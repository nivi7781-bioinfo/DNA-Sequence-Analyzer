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


else:
    print("Invalid DNA sequence")
