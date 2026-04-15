#predicate logic system

# step 1 create the class which will have methods to perfom operation on your knowledge base

class PrdicateLogicSystem:
    
    #constructor and self helps to create and access atribute of the class
    def __init__(self):
        #creating our attributes
        self.facts = {} # predicate : [values] ex rain : [yes]
        self.rules = [] # if premise -> then conclusion ex if rain then stayInside
        
    # method 1 for adding fact in out system
    
    def add_fact(self,predicate,value):
        
        # first creating predicate with empty value
        self.facts.setdefault(predicate,[]) # setdefault method agr key exist krti h to it will return it's value agr nhi krti to create one with default value
        
        #hume existing predicate pe overwrite nhi krna so agr predicate naya h to it will []
        if value not in self.facts[predicate]:
            self.facts[predicate].append(value)
    
    # method -2 for adding rule
    
    def add_rule(self , premise,conclusion ):
        self.rules.append((premise,conclusion))
    
    # method 3 to show all facts
    
    def show_facts(self):
        print("\nCurrent facts")
        for p,v in self.facts.items(): # dict.items() to fetch alll the pair
            print(p , end = " : ")
            print(v)
        
    
    # method 4- queuery check mtlb ye prediactae aur vlaue exist krti hai kya?
    
    def query(self,predicate,value):
        return value in self.facts.get(predicate,[])
        
    
    
    # method -5 forward chaining to create new facts from existing fact
    def infer(self):
            changed = True # to track new facts are added or not
            
            while changed: 
                changed = False # let's assume iss turn meinn koi naya rule add nhi hua
                
                # itterating over all the rule in self.rule
                
                for premises, conclusion in self.rules:
                    
                    # check jisa conclusion hmm add krne ka soch rhe uska premise hai already fact mein ya nhi
                    if premises in self.facts:
                        
                        # ab us fact ke sare value hum uske conclusion mein daalne ki kosis kareneg
                        
                        for val in self.facts[premises]:
                            
                            self.facts.setdefault(conclusion , []) # adding conclusion if not already there
                            
                            # adding tha value in conclusion from premises
                            
                            if val not in self.facts[conclusion]:
                                self.facts[conclusion].append(val)
                                changed = True # our assumption was wrong
                    
                    
#running the code 

# getting the object of clas

kb = PredicateLogicSystem()

while True:
    
    print("\n -- Predicate Logic System ---")
    print("1. Add Fact")
    print("2. Add rule (IF -> THEN)")
    print("3. Run Inference (Forward Chaining)")
    print("4. Query")
    print("5. Show Facts")
    print("6. Exit")
    
    choice = input("Enter your choice")
    
    if choice  == '1':
    
    elif choice == 2
    
    
    