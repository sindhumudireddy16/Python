#Library Management System
class LibRecord():  # class 1
    def __init__(self): # constructor
        pass

    def lib(self):
        __libName = "Mary" # Private data member
        print("Librarian name is",__libName)

class LibMembership():  #class 2
    memebfee="$150"
    def __init__(self): # constructor
       print("Membership fee: $150")

class MembershipFee(LibMembership):  #inheritance( #class 3)

    def __init__(self): #_init_ constructor
        LibMembership.__init__(self)

    def membershipFee(self,isPaid):
        self.isPaid=isPaid
        if (self.isPaid=="true"):
            print("Membership amount of",self.memebfee,"has been already paid")
        else:
            print("Membership amount of", self.memebfee, "not yet paid")

class patronDetails(): #class 4
    def __init__(self): #_init_ constructor
        pass

    def patronInfo(self, patronName,patronID):
        self.patronName = patronName
        self.patronID = patronID
        print("Student name is",self.patronName,"and student ID is",self.patronID)

class JournalDetails():    #class 5
    def __init__(self): #_init_ constructor
        pass

    def book(self,Journalname,JournalID,JournalAuthor):
        self.Journalname=Journalname
        self.JournalID=JournalID
        self.JournalAuthor=JournalAuthor
        print("Journal name: "+self.Journalname+"/ Book ID: "+self.JournalID+"/ Author: "+self.JournalAuthor)

class patronBookDetails(patronDetails,JournalDetails):   # multiple inheritance (#class 6)
    def __init__(self):     #_init_ constructor
        super().__init__()  # use of super keyword

    def JournalDates(self,borrowedOn,returnDate):
        self.borrowedOn = borrowedOn
        self.returnDate = returnDate
        print("The book was borrowed on "+self.borrowedOn+" and has to be returned on "+self.returnDate)
        print("------------------------------------------------------------------------------")

#instances of classes
lib1=LibRecord()
lib1.lib()
patron1=patronDetails()
patron1.patronInfo("Raji",16)
memberfee=MembershipFee()
memberfee.membershipFee("true")
book1=patronBookDetails()
book1.book("python","20000","jose")
book1.JournalDates("07-13-2017","07-23-2017")

lib1=LibRecord()
lib1.lib()
patron1=patronDetails()
patron1.patronInfo("swetha",18)
memberfee=MembershipFee()
memberfee.membershipFee("false")
book1=patronBookDetails()
book1.book("PDC","20002","Cory")
book1.JournalDates("08-6-2017","12-15-2017")

