FILE="book.txt"

def load_book():
    book_data={}
    try:
        with open(FILE,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                book_name,owner,status=line.split("|")
                book_data[book_name]=[owner,status]

    except FileNotFoundError:
        pass
    return book_data

def save_book(data):
    with open(FILE,"w",encoding="utf-8") as f:
        for name,info in data.items():
            user,status=info
            f.write(f"{name}|{user}|{status}\n")

def main():
    books=load_book()
    while True:
        print("\n=====图书借阅系统=====")
        print("1.新建图书")
        print("2.借阅图书")
        print("3.归还图书")
        print("4.查看全部图书")
        print("0.退出程序")
        try:
            opt=int(input("请输入功能序号："))
            if opt == 1:
                bk=input("输入图书名称：").strip()
                if bk=="":
                    print("图书名不能为空")
                if bk in books:
                    print("该图书已经录入！")
                    continue
                books[bk]=["无","在馆"]
                save_book(books)
                print("图书馆新增完成")

            elif opt==2:
                bk=input("要借阅的书名：").strip()
                if bk not in books:
                    print("不存在该书")
                    continue
                user,status=books[bk]
                if status=="已借出":
                    print(f"该书已经被{user}借走，暂时无法借阅")
                    continue
                borrow_user=input("输入借阅人的姓名：").strip()
                if borrow_user=="":
                    print("借阅人的名称不能为空")
                    continue
                books[bk]=[borrow_user,"已借出"]
                save_book(books)
                print("借阅成功")

            elif opt==3:
                bk=input("归还图书名称：").strip()
                if bk not in books:
                    print("无此图书记录")
                    continue
                user,status=books[bk]
                if status=="在馆":
                    print("该图书本来就在馆，无需归还")
                    continue
                books[bk]=["无","在馆"]
                save_book(books)
                print("归还成功")

            elif opt==4:
                if not books:
                    print("暂无图书数据")
                    continue
                print(f"\n{'书名':<10}{'借阅人':<6}{'状态'}")
                print("-"*25)
                for name,info in books.items():
                    u,s=info
                    print(f"{name:<10}{u:<6}{s}")

            elif opt==0:
                print("程序已退出，祝你生活愉快")
                break

            else:
                print("请输入0-4数字")

        except ValueError:
            print("输入必须是数字")

if __name__ == "__main__":
    main()








