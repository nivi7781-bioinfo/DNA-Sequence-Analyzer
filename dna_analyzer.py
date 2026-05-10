dna = input("Enter the DNA sequence: ").upper()

print("DNA Sequence:", dna)

if set(dna).issubset({"A", "T", "G", "C"}):
    print("Valid DNA sequence")

    print("Length of the given Sequence", len(dna))
    #count function
    print("A:", dna.count("A"))
    print("T:", dna.count("T"))
    print("G:", dna.count("G"))
    print("C:", dna.count("C"))
   #gc content calculation
    gc = dna.count("G") + dna.count("C")
    gccontent = (gc / len(dna)) * 100

    print("GC Content =", round(gccontent, 2), "%")

    reverse = dna[::-1]
    print("Reverse:", reverse)

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

    print("Complement:", comp)
     
    #dictionary
    count={
        "A":dna.count("A"),
        "T":dna.count("T"),
        "G":dna.count("G"),
        "C":dna.count("C")
        
    }
    print(count)
    
    #loop
    for key, value in count.items():
        print(key, "=", value)
        
        #sets
        bases={"A","T","G","C"}
        print(bases)
        print(set(dna))
    
    #loops
    count=0
    cnt=0
    for base in dna:
        if base=="A" or base=="G":
            count+=1
    print("Purine count=",count)
    for base in dna:
        if base=="T" or base=="C":
            cnt+=1
    print("Pyrimidine count=",cnt)
    
    rev=""
    for base in dna:
        rev=base+rev
    print("Reversed DNA Sequence=",rev)


else:
    print("Invalid DNA sequence")
    for base in dna:
        if base not in {"A","T","G","C"}:
            print("Invalid base found:", base)
            
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
                    
#dna validation
def dna_validate(dna):
    if set(dna).issubset({"A", "T", "G", "C"}):
        print("Valid DNA sequence")
        print("GC content:",gc_content(dna))
        print("Reversed DNA:",reverse(dna))
        print("Purine count:",purine(dna))
        print("Pyrimidine count:",pyrimidine(dna))
    else:
        print("INVALID DNA sequence")
        print(invalid_base(dna))
        
dna_validate(dna)
