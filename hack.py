import json
from datetime import  date ,datetime
def books():
    books=[]
    #add book function
    def add_book():
        
        print('enter books information:')
        book_id=input("book id")
        book_title=input("book title: ")
        book_author=input("book author :")
        book_subject=input("subject:")
        book_isbn=input("isbn :")
        book_price=input("price:")
        
        with open("books.json", "r") as file:
            books=json.load(file)
        for book in books:
            if(book['isbn']==book_isbn):
                print("books exists")
                return
            
        books.append({'id':book_id,'title':book_title,'author':book_author,'subject':book_subject,'isbn':book_isbn,'price':book_price,'copies':[{'id':'1','book_id':book_id,'rack':0,'status':False}]})

        with open("books.json", "w") as file:
            json.dump(books, file)
        #####################################################


    def manage_copies():
        book_id=input("enter book id to add")
        with open("books.json",'r') as file:
            books=json.load(file)
        for book in books:
            if book['id'] == book_id:
                print(book)
                copy_id = input("Enter copy id: ")
                copy_rack = input("Enter copy rack : ")
                copy_status = False
                book['copies'].append({'id': copy_id, 'book_id': book_id, 'rack': copy_rack, 'status': copy_status})

                with open("books.json", 'w') as file:
                    json.dump(books, file)

    def book_choices(book_choice):
        if(book_choice=='1'):
            add_book()
        elif(book_choice=='2'):
            manage_copies()
        else:
            print("enter valid input")

    while True:
        print("1.add books")
        print("2.manage copies")
        print("3.exit")
        book_choice=input("enter the choice")
        if(book_choice=='3'):
            break
        book_choices(book_choice)
##########################   Members ################

def members():
    members=[]
    def add_member():
        print('enter mebers information:')
        member_id=input("member id")
        member_name=input("member name: ")
        member_email=input("member email: ")
        member_phone=input("member phone: ")
        member_payment_date=str(date.today())
        member_paid_status=input("member paid status: ")

        with open("members.json", "r") as file:
            members=json.load(file)
        for member in members:
            if (member_id == member['id']):
                print("Member already exists")
                return
        members.append({'id': member_id, 'name': member_name, 'email': member_email, 'phone': member_phone, 'payment_date': member_payment_date, 'pd_s': member_paid_status})
        with open("members.json",'w') as file:
            json.dump(members, file)

    def edit_member():
        check_id = input("Enter the member id: ")
        with open("members.json", "r") as file:
            members = json.load(file)
        for member in members:
            if check_id == member['id']:
                member['email'] = input("Enter new email: ")
                member['phone'] = input("Enter new phone: ")
                
        with open("members.json", 'w') as file:
            json.dump(members, file)

    def member_choices(member_choice):
        if(member_choice=='1'):
            add_member()
        elif(member_choice=='2'):
            edit_member()
        else:
            print("Enter valid input")
    while True:
        print("1.add member")
        print("2.edit member")
        print("3.exit")
        member_choice=input("enter the choice")
        if(member_choice=='3'):
            break
        member_choices(member_choice)
##################### issue #################
    
def issue():
    issues = []
    members = []
    books = []
    def check_member():
        check_mem_id = input("Enter the member id: ")
        with open("members.json", "r") as file:
            members = json.load(file)
        for member in members:
            if check_mem_id == member['id']:
                print(member)
                break
        else:
            print("member not exists")

    def assign_copy():
        issue_id = input("Enter the issue id: ")
        copy_id = input("Enter the copy id: ")
        member_id = input("Enter member id: ")
        issue_date = str(date.today())
        returndue_date =issue_date[0:6]+issue_date[5:7]+str(int(issue_date[7:10])+7)
        return_date = "0"
        fine_amount = input("Enter the fine amount: ")

        with open("issues.json", "r") as file:
            issues = json.load(file)
        with open("members.json", "r") as file:
            members = json.load(file)
        with open("books.json", "r") as file:
            books = json.load(file)

        for book in books:
            for copies in book['copies']:
                
                if copies['id'] == copy_id and copies['status'] != True:
                    for member in members:
                        if member['id']  == member_id:
                            if member['pd_s'] == False:
                                print("member is not valid or not paid")
                            else:
                                copies['status'] = True
                                
                                issues.append({'id':issue_id, 'copy_id': copy_id, 'member_id': member_id,'issue_date': issue_date, 'return_duedate': returndue_date, 'return_date': return_date, 'fine_amount': fine_amount})
                                with open("issues.json", 'w') as file:
                                    json.dump(issues, file)
                                with open("books.json", 'w') as file:
                                    json.dump(books, file)
                                break
                        


                            


    def issue_choices(issue_choice):
        if issue_choice=='1':
            check_member()
        elif issue_choice=='2':
            assign_copy()
        else:
            print("Enter valid Input")
    while True:
        print("1. Check Member ")
        print("2. Assign copy ")
        print("3. exit")
        issue_choice = input("Enter your choice:")
        if(issue_choice == '3'):
            break
        issue_choices(issue_choice)

################### return ################################
def return1():
    issues=[]
    def return_choices(return_choice):
       
        def cal_fine():
            check_issue_id = input("Enter the issue id: ")
            dates = str(date.today())
            # print("dates",dates)
            with open("issues.json", 'r') as file:
                issues = json.load(file)  
            for issue in issues:
                if issue['id'] == check_issue_id:
                    # print("match")
                    day=issue['issue_date']
                    month=int(day[5:7])-int(dates[5:7])
                    fine_amt=month*5
                    ext_days=int(day[8:10])-int(dates[8:10])
                    
                    if ext_days > 7:
                        fine_amt = fine_amt +(ext_days - 7)*5
                        issue['fine_amount'] = fine_amt
                        print(f"Fine amount is {fine_amt}")
                        with open("issues.json", 'w') as file:
                            json.dump(issues, file)
                    else:
                        print("no fine")
                        issue['fine_amount'] = 0
                        with open("issues.json", 'w') as file:
                            json.dump(issues, file)

        def update_status():
            check_issue_id = input("Enter the issue id: ")
            with open("issues.json", 'r') as file:
                issues = json.load(file)
            with open("books.json", 'r') as file:
                books = json.load(file)
            for issue in issues:
                if issue['id'] == check_issue_id:
                    for book in books:
                        for copy in book['copies']:
                            if copy['id'] == issue['copy_id']:
                                copy['status'] = False
                                issue['return_date'] = str(date.today())
                                with open("issues.json", 'w') as file:
                                    json.dump(issues, file)
                                with open("books.json", 'w') as file:
                                    json.dump(books, file)
                                print("status updated")
                                break
            

        if return_choice=='1':
            cal_fine()
        elif return_choice=='2':
            update_status()
        else:
            print("Enter valid input!")
    while True:
        print("1. Calculate fine")
        print("2. Update status")
        print("3. Exit")
        return_choice = input("Enter your choice: ")
        if(return_choice == '3'):
            break
        return_choices(return_choice)
########################## payments ##############################
def payments():
    with open("payments.json", 'r') as file:
        payments = json.load(file)
    pay_id = input("Enter payment Id: ")
    pay_member_id = input("Enter payment member id: ")
    pay_amount = input("Enter payment amount: ")
    pay_type = input("Enter payment type : ")
    pay_trans_time = str(date.today())
    pay_nextdue = pay_trans_time[0:6]+str(int(pay_trans_time[5:7])+1)+pay_trans_time[7:10]
    with open("members.json", 'r') as file:
        members = json.load(file)
    for member in members:
        if member['id'] == pay_member_id:
            print(member)
            member['pd_s'] = True
            member['payment_date']=pay_trans_time
            with open("members.json", 'w') as file:
                json.dump(members, file)

    payments.append({'id': pay_id, 'member_id': pay_member_id, 'amt': pay_amount, 'type': pay_type, 'tran_time': pay_trans_time, 'next_pay_date': pay_nextdue})

    with open("payments.json", 'w') as file:
        json.dump(payments, file)

########################## reports ###############################
    
def reports():
    with open("books.json", 'r') as file:
        books=json.load(file)
    with open("issues.json", 'r') as file:
        issues=json.load(file)
    with open("members.json", 'r') as file:
        members=json.load(file)
    with open("payments.json", 'r') as file:
        payments=json.load(file)

    print("Report: ")
    
    print("book issued: ")

    for book in books:
        for copy in book['copies']:
            if copy['status'] == True:
                print(book['title'])
    print("Paid Members:")
    for member in members:
        
        if member['pd_s'] == True:
            print(member)
    amount = 0
    dates = str(date.today())
    print("dues :")
    for issue in issues:
        day=issue['issue_date']
        month=int(day[5:7])-int(dates[5:7])
        ext_days=int(day[8:10])-int(dates[8:10])
        if(ext_days>7 or month>0):
            print(issue)
        amount = amount + issue['fine_amount']
    print(f"The total fine amount is {amount}")



def choices(choice):
    if(choice=='1'):
        books()
    elif(choice=='2'):
        members()
    elif(choice=='3'):
        issue()
    elif(choice=='4'):
        return1()
    elif(choice=='5'):
        payments()
    elif(choice=='6'):
        reports()
    else:
        print("enter correct input")
##########################   menu #############################   
def menu():
    while True:
        print("options :")
        print("1.books")
        print("2.members")
        print("3.issue")
        print("4.return")
        print("5.payments")
        print("6.reports")
        print("7.exit")
        choice =input("enter the choice :")
        if(choice=='7'):
            break
        choices(choice)

print("enter the login  details (name=lib ,pasword=123456 ):")
login_name=input("enter the name:")
login_paswwd=input("enter the password:")
passw='123456'
if(login_name=="lib" and login_paswwd==passw):
    menu()
else:
    print("Worng credentials")



    


