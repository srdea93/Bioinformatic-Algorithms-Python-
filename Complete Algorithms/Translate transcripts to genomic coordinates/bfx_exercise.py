### Author: Steven Dea
### Latest update: 05/05/22
### Project: BFX Exercise

### This script is a command-line use Python script to translate -based transcript coordinates
### to 0-based genomic coordinates.

### ASSUMPTIONS:
### CIGAR string only contains integer values and chars: "M, D, I"
### Transcript name and Chromosome name are either string values or are correctly matched integer values
### i.e. ('TR1' or '1' or 1 & 'CHR1', '1', or 1)
### Transcript start coordinate and chromosome coordinates will be interger values but can be either stored as ints or strings
### Space complexity isn't an issue

### TESTING PLAN:
### 0. Input files are correct
### 1. Input files are missing
### 2. Input files are empty
### 3. Input files have duplicates
### 4. Input files have no overlapping transcripts so output is empty
### 5. Input files contain incorrect data types in any of the columns
### 6. Input files contain transcript coordinates that do NOT match the transcript mapping
### 7. Input files contain CIGAR with invalid strings
### 8. Input files contain only specific rows with missing values
### 9. Input files contain chr or transcript coordinates that are not integers

### Total time spent - 4.5 hours
import pandas as pd
import argparse
import time
import sys

# ---------- READ & REFORMAT INPUTS ----------
def read_and_format_inputs(input_1, input_2):
    """
    Take both input files and reformat them into pandas dataframes with proper column headers, then return as a list of dataframes.
    
        Parameters:
            input_1 (.tab file): 4 column tab-delimited file containing mappings - (Col 1) transcript, (Col 2) chromosome name,
                                (Col 3) 0-based starting position on chromosome, (Col 4) CIGAR string indicating the mapping
            input_2 (.tab file): 2 column tab-delimited file containing queries - (Col 1) transcript, 
                                (Col 2) 0-based transcript coordinate

            Returns: 
            reformatted_input_1_df, reformatted_input_2_df (dataframes):  2 pandas dataframes with 
                                                                        column headers of both input files
    """
    # read in both input files as dataframes
    try:
        reformatted_input_1_df = pd.read_csv(input_1, sep='\t', header=None)
    except FileNotFoundError as e:
        print("Input file 1 not found!\nExiting script.")
        sys.exit(1)
    except pd.io.common.EmptyDataError:
        print("Input file 1 is empty\nExiting script.")
        sys.exit(1)

    try:
        reformatted_input_2_df = pd.read_csv(input_2, sep='\t', header=None)
    except FileNotFoundError as e:
        print("Input file 2 not found!\nExiting script.")
        sys.exit(1)
    except pd.io.common.EmptyDataError:
        print("Input file 2 is empty\nExiting script.")
        sys.exit(1)

    # remove null values
    reformatted_input_1_df.dropna(axis=0, inplace=True)
    reformatted_input_2_df.dropna(axis=0, inplace=True)

    # remove duplicate rows
    reformatted_input_1_df.drop_duplicates(inplace=True)
    reformatted_input_2_df.drop_duplicates(inplace=True)

    # check lengths of input files to make sure they aren't empty
    if len(reformatted_input_1_df) < 1 or len(reformatted_input_2_df) < 1:
        print("One or more input files is empty!\nExiting script.")
        sys.exit(1)
    
    # reformat input 1 to contain the correct column headers
    reformatted_input_1_df = reformatted_input_1_df.rename(columns={0: 'transcript', 1: 'chromosome', 2: 'chr_coordinate', 3: 'cigar'})
    # reformat input 2 to contain the correct columm headers
    reformatted_input_2_df = reformatted_input_2_df.rename(columns={0: 'transcript', 1: 'transcript_coordinate'})
    
    return reformatted_input_1_df, reformatted_input_2_df


# ---------- MERGE REFORMATTED INPUTS ----------
def merge_inputs(reformatted_input_1_df, reformatted_input_2_df):
    """
    Merge both reformatted input dataframes using a left (input 2) outer merge
     to generat an output dataframe that contains transcript, transcript coordinate, chromosome, chromosome coordinate, CIGAR
        
        Parameters: 
            reformatted_input_1_df (pandas dataframe): input_1 reformatted as a dataframe with proper column headers
            reformatted_input_2_df (pandas dataframe): input_2 reformatted as a dataframe with proper column headers
        
        Returns:
            merged_input_df (pandas dataframe): reformatted_input_1_df and reformatted_input_2_df right inner merged
                                                on transcript column. 4 columns: (Col 1) transcript, (Col 2) transcript
                                                coordinate, (Col 3) chromosome, (Col 4) chromosome coordinate, (Col 5) CIGAR
    """
    # merge input dataframes
    merged_input_df = reformatted_input_2_df.merge(reformatted_input_1_df[['transcript', 'chromosome', 'chr_coordinate', 'cigar']], how='left',
                                                        left_on='transcript', right_on='transcript')
    # reorder columns
    merged_input_df = merged_input_df[['transcript', 'transcript_coordinate', 'chromosome', 'chr_coordinate', 'cigar']]

    # transcript coordinate & chr coordinate to numeric, cast to None if value can't be cast as numeric and then remove
    merged_input_df['transcript_coordinate'] = pd.to_numeric(merged_input_df['transcript_coordinate'], errors='coerce', downcast='integer')
    merged_input_df['chr_coordinate'] = pd.to_numeric(merged_input_df['chr_coordinate'], errors='coerce', downcast='integer')

    # remove null values
    merged_input_df.dropna(axis=0, inplace=True)
    
    return merged_input_df


# ---------- TRANSLATE COORDINATES ----------
transcript_cigar_dict = {'M': 'g', 'D': '-', 'I': 'g'}
chromosome_cigar_dict = {'M': 'g', 'D': 'g', 'I': '-'}

# convert cigar into a transcript string with 'g' simulating a base and - simulating an empty space
def cigar_to_string(cigar, cigar_to_string_dict):
    """
    Given an input CIGAR string, transform it into a transcript and chromosome strings. Save it in a hashtable
    so transformations aren't done multiple times if unecessary.

        Parameters:
            cigar (string): CIGAR string found in the "cigar" column of merged_input_df
            cigar_to_string_dict (dictionary): hashtable storing CIGAR strings as keys and transformed CIGAR to
                                                transcript and chromosome strings stored as a tuple

        Returns:
            transcript_string (string): transformed CIGAR string to represent transcript as a string
            chromosome_string (string): transformed CIGAR string to represent chromosome as a string                                      
    """
    # don't need to calculate it if it's already in the hashtable
    if cigar in cigar_to_string_dict:
        return cigar_to_string_dict[cigar][0], cigar_to_string_dict[cigar][1]
    else:
        transcript_string, chromosome_string = "", ""
        integer_index_start, integer_index_end = 0, 0

        for i in range(len(cigar)):
            if not cigar[i].isdigit():
                # check if the letter is in our dictionaries, if not, return error & return null
                if cigar[i] not in chromosome_cigar_dict:
                    print("Invalid CIGAR string\nReturning None")
                    return None, None
                integer_index_end = i
                integer = int(cigar[integer_index_start:integer_index_end])
                
                # add to transcript and chromosome strings the # of g's or -'s
                add_transcript_string = F"{integer*transcript_cigar_dict[cigar[i]]}"
                transcript_string += add_transcript_string
                
                add_chromosome_string = F"{integer*chromosome_cigar_dict[cigar[i]]}"
                chromosome_string += add_chromosome_string
                
                # set new start
                integer_index_start = i + 1
                
        return transcript_string, chromosome_string
    
    
def translate_transcript(transcript_string, chromosome_string, transcript_start, transcript_coordinate):
    """
    Translate transcript coordiantes by performing a vectorized calculation of adding the transcript coordinate column
    to the chromosome coordinate column.

        Parameters:
            transcript_string (string): transformed CIGAR string to represent transcript as a string
            chromosome_string (string): transformed CIGAR string to represent chromosome as a string  
            transcript_start (int): integer that represents the index that a transcript starts on its corresponding
                                    chromosome
            transcript_coordinate (int): integer that represents where the target transcript index lies to be translated
                                        to chromosome index

        Returns:
            chromosome_index (int): integer that represents the translated transcript index to chromosome index
    """
    chromosome_index = transcript_start
    transcript_index = 0

    for transcript_base, chromosome_base in zip(transcript_string, chromosome_string):
        # check to make sure the transcript index hasn't matched transcript coordinate yet
        if transcript_index < transcript_coordinate:
            # make sure as we iterate through both depending on if at that if either has a 'g' then we
            # increase the index by one, if '-' pass
            if transcript_base == 'g':
                transcript_index += 1
            if chromosome_base == 'g':
                chromosome_index += 1
        else:
            break 
    # check if the index has reached the coordinate by the end. If not, exit.
    if transcript_index < transcript_coordinate:
        print("Transcript coordinate does not lie within transcript!\nExiting script.")
        sys.exit(1)
    return chromosome_index


# ---------- DRIVER ----------
def driver(input_1, input_2, output):
    """
    Driver function to run script.
    1. Read and reformat input files and check they are acceptable formats to be used for script.
    2. Merge reformatted input files
    3. Transform CIGAR to strings
    4. Translate transcript coordinates
    5. Save output file

        Parameters
            input_1 (.tab file): 4 column tab-delimited file containing mappings - (Col 1) transcript, (Col 2) genomic mapping,
                               (Col 3) 0-based starting position on chromosome, (Col 4) CIGAR string indicating the mapping
            input_2 (.tab file): 2 column tab-delimited file containing queries - (Col 1) transcript, 
                                (Col 2) 0-based transcript coordinate
            output (.tab file): Output file name
        
        Returns:
            done (int): returns a 0 if succeeds, or a 1 if fails
    """
    script_start = time.perf_counter()
    print(F"-----INPUTS-----")
    print(F"Input 1: {input_1}\nInput 2: {input_2}")


    print(F"\n-----READ AND REFORMAT-----")
    reformatted_input_1_df, reformatted_input_2_df = read_and_format_inputs(input_1, input_2)
    print(F"Reformatted input 1 df size: {len(reformatted_input_1_df)}")
    print(F"Reformatted input 2 df size: {len(reformatted_input_2_df)}")


    print(F"\n-----MERGE-----")
    merged_input_df = merge_inputs(reformatted_input_1_df, reformatted_input_2_df)
    print(F"Merged df size: {len(merged_input_df)}")
    if len(merged_input_df) < 1:
        print("Merged dataframe has no values!\nExiting script.")
        sys.exit(1)

    print(merged_input_df.head())


    print(F"\n-----CIGAR TO STRING AND TRANSLATE-----")
    # iterate through all cigars, transcript coordinates, and transcript starts
    # in the dataframe to calculate the strings and store in a hashtable and then
    # translate the transcript coordinate to chromosome index
    # cigar to string
    cigar_to_string_dict = {}
    cigars = list(merged_input_df['cigar'])
    transcript_coordinates = list(merged_input_df['transcript_coordinate'])
    transcript_starts = list(merged_input_df['chr_coordinate'])
    translated_chromosome_coordinates = []

    for cigar, transcript_coordinate, transcript_start in zip(cigars, transcript_coordinates, transcript_starts):
        transcript_string, chromosome_string = cigar_to_string(cigar, cigar_to_string_dict)
        # If the cigar string contains improper string values
        if transcript_string is None or chromosome_string is None:
            translated_chromosome_coordinates.append(None)
        else:
            # add cigar key and string values if not in hashtable
            if cigar not in cigar_to_string_dict:
                cigar_to_string_dict[cigar] = (transcript_string, chromosome_string)
            
            # translate
            translated_chromosome_coordinate = translate_transcript(transcript_string, chromosome_string, transcript_start, transcript_coordinate)
            translated_chromosome_coordinates.append(translated_chromosome_coordinate)

    merged_input_df['translated_chr_coordinate'] = translated_chromosome_coordinates

    # remove null values
    merged_input_df.dropna(axis=0,inplace=True)

    # cast coordinate values to ints
    merged_input_df['transcript_coordinate'] = merged_input_df['transcript_coordinate'].astype(int)
    merged_input_df['translated_chr_coordinate'] = merged_input_df['translated_chr_coordinate'].astype(int)
    
    
    print(F"\n-----TRANSLATED DF-----")
    # drop unecessary columns
    output_df = merged_input_df.drop(columns=['cigar', 'chr_coordinate'])
    # drop any null values
    output_df.dropna(axis=0, inplace=True)
    print(F"Translated df size: {len(output_df)}")
    print(output_df.head())

    print(F"\n-----SAVING-----")
    output_df.to_csv(output, sep='\t', index=False, header=False)
    print(F"File saved to: {output}")

    print(F"\n-----PERFORMANCE-----")
    script_end = time.perf_counter()
    print(F"{script_end - script_start} ms")
    
    return 0


# ---------- MAIN ----------
def main():
    """
    Function that allows script to be called in the command line

        Parameters:
            input_1 (.tab file): 4 column tab-delimited file containing mappings - (Col 1) transcript, (Col 2) genomic mapping,
                                (Col 3) 0-based starting position on chromosome, (Col 4) CIGAR string indicating the mapping
            input_2 (.tab file): 2 column tab-delimited file containing queries - (Col 1) transcript, 
                                (Col 2) 0-based transcript coordinate
            output (.tab file): Output file name

        Returns:
            NONE
            
    """
    args = argparse.ArgumentParser()
    # arguments go here
    args.add_argument("--input_1", action="store", required=True)
    args.add_argument("--input_2", action="store", required=True)
    args.add_argument("--output", action="store", required=True)
    options = args.parse_args()

    # final function goes here
    driver(options.input_1, options.input_2, options.output)


if __name__ == "__main__":
    main()