#modular functions
#gc gc_content
def gc_content(dna):
    gc=dna.count("G") + dna.count("C")
    return (gc / len(dna)) * 100

#reverse dna
def reverse(dna):
    return dna[::-1]

#purine count
def purine(dna):
    count=0
    for base in dna:
        if base=="A" or base=="G":
            count+=1
    return count

#pyrimidine count
def pyrimidine(dna):
    cnt=0
    for base in dna:
        if base=="T" or base=="C":
            cnt+=1
    return cnt

#invalid base
def invalid_base(dna):
            for base in dna:
                if base not in {"A","T","G","C"}:
                    return f"Invalid base:{base}"

#complementary dna
def complement(dna):
    comp = ""
    for base in dna:
        if base == "A":
            comp += "T"
        elif base == "T":
            comp += "A"
        elif base == "G":
            comp += "C"
        elif base == "C":
            comp += "G"
    return f"Complement:{comp}"
                    
#dna validation
def dna_validate(dna):
    if set(dna).issubset({"A", "T", "G", "C"}):
        print("Valid DNA sequence")
        print("GC content:",gc_content(dna))
        print("Reversed DNA:",reverse(dna))
        print("Purine count:",purine(dna))
        print("Pyrimidine count:",pyrimidine(dna))
        print(complement(dna))
    else:
        print("INVALID DNA sequence")
        print(invalid_base(dna))

dna = input("Enter the DNA sequence: ").upper()    
dna_validate(dna)
