from tkinter import *



class MyGUI:
    def __init__(self):
        self.root=Tk()
        self.root.title('Loan calculator')
        Label(self.root,text='Annual Interest rate').grid(row=1,column=1,sticky=W)
        Label(self.root,text='Number of year').grid(row=2,column=1,sticky=W)
        Label(self.root,text='Loan amount').grid(row=3,column=1,sticky=W)
        Label(self.root,text='Monthly Payment').grid(row=4,column=1,sticky=W)
        Label(self.root,text='Total payment').grid(row=5,column=1,sticky=W)
        self.anualIncome=StringVar()
        Entry(self.root,textvariable=self.anualIncome,justify=RIGHT).grid(row=1,column=2,sticky=E)
        self.noYear=StringVar()
        Entry(self.root,textvariable=self.noYear,justify=RIGHT).grid(row=2,column=2,sticky=E)
        self.loanAmt=StringVar()
        Entry(self.root,textvariable=self.loanAmt,justify=RIGHT).grid(row=3,column=2,sticky=E)
        # Monthly payment
        self.monPay=StringVar()
        monLable=Label(self.root,textvariable=self.monPay).grid(row=4,column=2,sticky=E)
        # Total pay
        self.totalPay=StringVar()
        totLabel=Label(self.root,textvariable=self.totalPay).grid(row=5,column=2,sticky=E)


        btncomp=Button(self.root,text='Compute Payment',command=self.computePayment).grid(row=7,column=2,sticky=E)
        self.root.mainloop()
    def computePayment(self):
        # print(self.anualIncome.get())
        # print(self.noYear.get())
        # print(self.loanAmt.get())
        monthPay = self.getMontlyPayment(float(self.loanAmt.get()),float(self.anualIncome.get())/1200,int(self.noYear.get()))
        self.monPay.set(format(monthPay,"10.2f"))
        total = float(self.monPay.get())*12*int(self.noYear.get())
        self.totalPay.set(format(total,"10.2f"))

    def getMontlyPayment(self,loanAmt,monthlyInt,years):
        monthly = loanAmt*monthlyInt/(1-1/(1+monthlyInt)**(years*12))
        return monthly

MyGUI()