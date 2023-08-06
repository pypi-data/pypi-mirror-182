# generator for reading fasta files
# returns header and seq


def fasta_generator(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        read = ""

        # read sequences into a numpy array
        for line in lines:
            if not line.startswith('>'):
                read += line.rstrip('\n')
            if line.startswith('>') or line == lines[-1]:
                if line.startswith('>'):
                    header = line.strip()
                if(read != ""):
                    read = read.strip()
                    yield header, read
                    read = ""
                
        