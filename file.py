try:
    filename=input("Enter file name:")
    data=input("Enter text:")
    if filename=="":
        raise Exception("File name could not empty")
    f=open(filename,"w")
    f.write(data)
    print("Data written successfully")
except Exception as e:
    print("Error:",e)
finally:
    try:
        f.close()
        print("file closed")
    except:
        print("file not created")
