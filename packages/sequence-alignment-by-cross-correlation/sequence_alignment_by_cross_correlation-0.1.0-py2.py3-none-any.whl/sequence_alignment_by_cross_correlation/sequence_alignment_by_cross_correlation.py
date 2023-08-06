""" 
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX0kxdllccccclodxk0XNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXKkdc;'';:ccccclc:,',;lxKNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNX0kxl;',:oxO0XXXXXXXXK0Oxl,':OXN
NNNNNNNNNNNNNNNNNNNNNNNNNX0xc,'';lxOKNNNNNNNNNNNNNNNNXd,.lKN
NNNNNNNNNNNNNNNNNNNNNNNKkl;';lox0OdkXNNNNNNNNNNNNNNNNXd'.lKN
NNNNNXNNNNNNNNNNNNNNXKx:'';d0XNNXo.,kNNNNNNNNNNNNNNNKx;.,xXN
NNNXxcxXNNNNNNNNNNXOo;',cxOXNNNNXo.'xNNNNNNNNNNNXKOd:'.,dKNN
NNNKc.c0NNNNNNNNKkc'';oOKx:oKNNNXo.'xXNNNXXXKOxoc;'.':d0XNNN
NNNO;.:0NNNNNXOo:',cx0XNN0xkXNNNXo.'okxdlcc:;'.',:ldOXNNNNNN
NNNk;.c0NNX0xc'';oOKNNNNNXXKOxddl,..''.',;:codxO0XXNNNNNNNNN
NNNKo',ldoc,',cxKNNNXKOxoc:;'..''...;oxO0KX0OOOOO00000KXNNNN
NNNNKxc;,,;ldOXXKOxoc;'.',:loxxkOc..oXNNNNKo,''',,,,;ckXNNNN
NNNNNNXKKKKXX0dc;''';cloxOXXNNNNXl..oXNNNNXKxlc:;,',;ckXNNNN
NNNNNNNNNX0xl,.';cdOKXO:,dXNNNNNXo..oXNNNNNNKd,'',;::cx0KXNN
NNNNNNNXOo;'.;lkKXNNNNk,.lKNNNNNXo..oXNNNNN0dl;,,;;::;;;oKNN
NNNNNX0o,.'cx0XNNNNNNNO;.c0NNNNNXo.'dXNNNNN0l;;;::cclodkKNNN
NNNNKd;',lkXNNNNNNNNNNO;.c0NNNNNKo..dXNNNNNNXKKXXXXXNNNNNNNN
NNNNx;,lOXNNNNNNNNNNNNXkokXNNNNNXk:;kNNNNNNNNNNNNNNNNNNNNNNN
NNNNX00XNNNNNNNNNNNNNNNNNNNNNNNNNXKKXNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
"""
#################################
#                               #
#            imports            #
#                               #
#################################
#import typer to make a nice CLI
import typer

#colors
from rich import print as prnt

#use numpy fot the number magic
import numpy as np

#plotting graphs with
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings( "ignore", module = "matplotlib\..*" )

#for timing and naming
from datetime import datetime

#for getting the cwd
import os

#################################
#                               #
#          definitions          #
#                               #
#################################

#Defining dicts for DNA and RNA
basenDNA = {
  "A": "T",
  "G": "C",
  "T": "A",
  "C": "G",
  "N": "N",
}

basenRNA = {
  "A": "U",
  "G": "C",
  "U": "A",
  "C": "G",
  "N": "N",
}


#create an instance of typer
app = typer.Typer()

#################################
#                               #
#           functions           #
#                               #
#################################

def verify(sequence: str) -> list:
    '''This code verfies if a sequence is a DNA or RNA'''
    #convert the input sequence to a set
    #this reduces the string into a set with all unique chars e.g. set('ACACTATCTAG') is {'A', 'C', 'G', 'T'}
    seq = set(sequence)

    #now we see if our seq set is a subset {"A", "T", "C", "G", "N"}
    #its important to check for the subset, because a sequence like "CGNNNNNNNCG" would not be verified if we would compare the union
    if seq.issubset({"A", "T", "C", "G", "N"}):
        return [True, "DNA"]
    
    #same works for RNA
    if seq.issubset({"A", "U", "C", "G", "N"}):
        return [True , "RNA"]
    #othersequences are rejected with this answer:
    else:
        return [False, "Invalid sequence"]

#This function translates each base in a complex number representation
def transform(seq: str) -> str:
    trans_seq = []
    #this check is not really needed, but its nice to have
    if verify(seq)[1] == 'DNA':
        #replace the chars with the corresponding Base
        seq = [sub.replace('A', '0+1j').replace('T', '0-1j').replace('G', '1+0j').replace('C', '-1+0j').replace('N', '+0+0j') for sub in list(seq)]
    elif verify(seq)[1] == 'RNA':
        #replace the chars with the corresponding Base
        seq = [sub.replace('A', '0+1j').replace('U', '0-1j').replace('G', '1+0j').replace('C', '-1+0j').replace('N', '+0+0j') for sub in list(seq)]
    
    #since replace wont take anything else than str, we need to convert before returning it
    for c in seq:
        trans_seq.append(complex(c))
    return trans_seq

#reverse a string
def reverse(seq: str) -> str:
    '''This function returns a reverse complement
    of a DNA or RNA strand'''
    #this walkes though the list from start to finish with the step size -1 (aka, reversing)
    seq = seq[::-1]
    return seq

#Compliment generator
def compliment(seq: str) -> str:
    '''This function returns a reverse complement
    of a DNA or RNA strand'''
    #See if sequence is valid
    verified = verify(seq)
    if verified[1] == "DNA":

        # complement the strand
        # only upper sequence to not have to deal with this herdal
        seq = seq.upper()
        #switch bases and join them together
        seq = ''.join(basenDNA.get(ch) for ch in seq)
        return seq
 
    elif verified[1] == "RNA":

        # complement strand
        # only upper sequence to not have to deal with this herdal
        seq = seq.upper()
        #switch bases and join them together
        seq = ''.join(basenRNA.get(ch) for ch in seq)
        return seq

    else: 
        prnt(":heavy_exclamation_mark: Invalid sequence")

#Reads the file and cleans it up
def openAsFile(filepath: str) -> str:
    #opens the file and joins the lines together in a header part and a sequnce part
    #TODO: Deal with white spaces at the end and also deal with multiple sequnces in one file
    file = open(filepath)
    selection = file.read()
    file.close()
    lines = selection.split('\n')
    header = ''.join(lines[0])
    sequence = ''.join(lines[1:])
    return header, sequence

def saveAsFile(information: list, filepath: str) -> None:
    #write the list of information in a file

    fileToSave = open(filepath, 'w')
    
    for info in information:
        fileToSave.writelines(info)
    
    fileToSave.close()

def evalResults(correlate1: np.array, correlate2: np.array, b_shift_positions: np.array) -> np.array:
    x = b_shift_positions
    y1 = correlate1
    y2 = correlate2

    #for y1 calculate some statistical values:
    y1_avg = np.average(correlate1)
    y1_prct80 =np.percentile(y1,80)
    y1_std = np.std(y1)
    y1_limit = 4*(y1_std+y1_avg) + y1_prct80
    numberOfPeaks_y1 = sum(y1 > y1_limit)

    #for y2 calculate some statistical values:
    y2_avg = np.average(correlate2)
    y2_prct80 =np.percentile(y2,80)
    y2_std = np.std(y2)
    y2_limit = 4*(y2_std+y2_avg) + y2_prct80
    numberOfPeaks_y2 = sum(y2 > y2_limit)

    #draw a plot with the data
    figure, axis = plt.subplots(1, 2)

    axis[0].plot(x, y1)
    axis[0].plot([x[0],x[-1]], [y1_limit,y1_limit])
    axis[0].set_title("correlation1")
  
    axis[1].plot(x, y2)
    axis[1].plot([x[0],x[-1]], [y2_limit,y2_limit])
    axis[1].set_title("correlation2")
    
    #here we evaluate what a peak is
    #if one or both #peaks are zero, this could mean that we have a clear peak (if not both are zero (case is not catches here))
    if numberOfPeaks_y1 == 0 or numberOfPeaks_y2 == 0:
        prnt(':sparkles: Clean result')

        #the correlation with the highest number of peaks wins the race
        if numberOfPeaks_y1 > numberOfPeaks_y2:
            #the highest peaks will be returned
            prnt(f':point_right: Die höchste Übereinstimmung mit einem score von {correlate1[correlate1.argmax()]} ist bei einer Verschiebung von {b_shift_positions[correlate1.argmax()]} bp vorhanden')
            return y1, b_shift_positions[correlate1.argmax()], numberOfPeaks_y1, 1
        elif numberOfPeaks_y2 > numberOfPeaks_y1:
            #the highest peaks will be returned
            prnt(f':point_right: Die höchste Übereinstimmung mit einem score von {correlate2[correlate2.argmax()]} ist bei einer Verschiebung von {b_shift_positions[correlate2.argmax()]} bp vorhanden')
            return y2, b_shift_positions[correlate2.argmax()], numberOfPeaks_y2, 2
        else:
            #in this case both of correlations did not return any peaks
            #this is where we take the highest correlation result and return it 
            prnt(':heavy_exclamation_mark: No result was found, check the limit!')
            prnt(':heavy_exclamation_mark: Fallbackmethod initiated!')
            prnt(':heavy_exclamation_mark: Since there was no match found, the result with the highest score will make the race. Check the graphs to know whats going on :)')
            #we will tell the user the highest result for each correlation
            prnt(f' :keycap_digit_one: Eine Übereinstimmung mit einem score von {y1[y1.argmax()]} ist bei einer Verschiebung von {b_shift_positions[y1.argmax()]} bp vorhanden')
            prnt(f' :keycap_digit_two: Die zweite Übereinstimmung mit einem score von {y2[y2.argmax()]} ist bei einer Verschiebung von {b_shift_positions[y2.argmax()]} bp vorhanden')
            
            if y1.argmax() >= y2.argmax():
                return y2, b_shift_positions[correlate2.argmax()], numberOfPeaks_y2, 2
            else:
                return y1, b_shift_positions[correlate1.argmax()], numberOfPeaks_y1, 1
    else:
        prnt(':heavy_exclamation_mark: We need to work on the limit :/')

def calcScore(seq1: str,seq2: str):
    #this calculates the similarity of the two sequnces on a base to base bassis

    #asser as sanity check
    assert len(seq1) == len(seq2)
    total = len(seq1)
    
    matches = 0
    #count matches
    for i in range(total):
        if seq1[i] == seq2[i] or seq1[i] == 'N' or seq2[i]=='N':
            matches += 1

    return matches, total


#################################
#                               #
#            command            #
#                               #
#################################

#This signals out CLI to make this an executable command
@app.command()
def align(inputseq1: str, inputseq2: str):
    #Check if the sequence is DNA/RNA
    if verify(inputseq1)[0] == True:
        seq1 = inputseq1
        prnt(f":white_check_mark: [bold green]Klappt![/bold green] [white]Sequenz 1 wurde importiert[/white]")
        prnt(f':dna: Es handelt sich um [bold green]{verify(seq1)[1]}[/] mit einer Länge von [yellow]{len(seq1)} bp[/]')

    #If not, interprete as a file
    else:
        try:
            head1, seq1 = openAsFile(inputseq1)
            prnt(f":white_check_mark: [bold green]Klappt![/bold green] [white]Sequenz 1 [bold green]{head1}[/] wurde importiert[/white]")
            prnt(f':dna: Es handelt sich um [bold green]{verify(seq1)[1]}[/] mit einer Länge von [yellow]{len(seq1)} bp[/]')

        except:
        #If its not interpreteable as a file -> Error
            prnt("[bold red]Alert![/bold red] [red]Sequenz 1 konnte nicht interpretiert werden[/red] damn! :boom:")
    
    #same as with inputseq1...
    if verify(inputseq2)[0] == True:
        seq2 = inputseq2
        prnt(f":white_check_mark: [bold green]Klappt![/bold green] [white]Sequenz 2 wurde importiert[/white]")
        prnt(f':dna: Es handelt sich um [bold green]{verify(seq2)[1]}[/] mit einer Länge von [yellow]{len(seq2)} bp[/]')
    else:
        try:
            head2, seq2 = openAsFile(inputseq2)
            prnt(f":white_check_mark: [bold green]Klappt![/bold green] [white]Sequenz 2 [bold green]{head2}[/] wurde importiert[/white]")
            prnt(f':dna: Es handelt sich um [bold green]{verify(seq2)[1]}[/] mit einer Länge von [yellow]{len(seq2)} bp[/]')

        except:
            prnt("[bold red]Alert![/bold red] [red]Sequenz 2 konnte nicht interpretiert werden[/red] damn! :boom:")

    #the longer sequence should be seq1
    if len(seq2) > len(seq1):
        seq1, seq2 = seq2, seq1
        #string inputs (not files) have no header and this is why we need to mitigate this with "try"
        try:
            head1, head2 = head2, head1
        except:
            pass
        prnt(f":repeat: [bold yellow]Achtung![/bold yellow] [white]Die Sequenzen wurden getauscht (1 -> 2 und 2 -> 1)[/white]")

    #If both of the sequences are loaded, transform them into a complex representation
    a = np.array(transform(seq1))
    b = np.array(transform(seq2))

    #create a reverse compliment to check if the sequence is present in the complimentary strand
    seq2_rc = reverse(compliment(seq2))
    rc_b = np.array(transform(seq2_rc))

    #create the correlation matrix for a and b and for a and the reverse compliment of b
    prnt(f":information_desk_person: [white]Es werden zwei correlation Matrices erstellt. Correlation2 nutzt dabei das reverse compliment der Sequenz2[/white]")
    correlate_result1 = np.correlate(a, b, 'full')
    correlate_result2 = np.correlate(a, rc_b, 'full')

    #create the shifts the correlationmatrix used
    b_shift_positions = np.arange(-len(a) + 1, len(b))

    #evaluate the results of both correlations for peaks and return the best match
    y, shift, numberPeaks, num = evalResults(correlate_result1, correlate_result2, b_shift_positions)

    #calculate the start and end position on the bigger sequence
    endpos_sequence = len(a) + shift
    startpos_seqence = endpos_sequence - len(b)

    #sanity check again
    assert endpos_sequence - startpos_seqence == len(seq2)

    #num is the correlation that contained the highest peak
    if num == 1:
        #use datetime to create unique filenames
        dataending = datetime.now().strftime('results/sequenceallignment_%d%b%Y_%H_%M_%S.txt')
        saveAsFile([seq1[startpos_seqence:endpos_sequence]+'\n', seq2[:]],dataending)
        matches, total = calcScore(seq1[startpos_seqence:endpos_sequence],seq2[:])
    elif num == 2:
        dataending = datetime.now().strftime('results/sequenceallignment_%d%b%Y_%H_%M_%S.txt')
        saveAsFile([seq1[startpos_seqence:endpos_sequence]+'\n', seq2_rc[:]],dataending)
        matches, total = calcScore(seq1[startpos_seqence:endpos_sequence],seq2_rc[:])
    #+1 because of the index starting at 0, but the bp refference starts a 1 in most tools
    prnt(f':flag_in_hole: The matching sequnce starts at the index {startpos_seqence+1} and ends at {endpos_sequence+1}')
    prnt(f':slot_machine: The number of matching basepairs for a shift of {shift} is {matches}/{total} ≈ {round((matches/total)*100,2)}%')
    prnt(f':file_folder: Your file was saved at {os.getcwd()}/{dataending}')
    plt.show()

if __name__ == '__main__':
    app()