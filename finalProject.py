import cv2

vid = "startup.MOV"
def video():
    cap = cv2.VideoCapture(vid)
    while(cap.isOpened()):
        ret,frame = cap.read()
        frame = cv2.resize(frame, (1200, 700))
        cv2.imshow("video",frame)
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

video()
option1 = input("\nYou work at a big corporation that deals with programming and such (duh). During one particularly hard point in your project, you are tempted to let Chat GPT help you in writing your code. But only for help, of course. Do you use Chat GPT? 'y' or 'n'\n")

if option1 == "y":
    vid = "option1YES.MOV"
    video()
    option2Yes = input("\nYou put in a prompt, and the AI gives you a full answer, all of your code is written! You can either copy and paste all of it, or decide against using it. Will you use it? 'y' or 'n'\n")
    if option2Yes == "y":
        vid = "option2YES.MOV"
        video()
        print("\nYou sumbit the code, getting it in way before the deadline. Unfortunately, the code is full of errors and your bosses figured out you used AI. You're fired, and can't find any other programming job elsewhere for your lack of creativity.\n")
    elif option2Yes == "n":
        vid = "option2NO.MOV"
        video()
        print("\nYou have the answer in front of you but you don't decide to paste it. Though, you do take ideas from the code given and eventually submit a successful program by the deadline.\n")

elif option1 =="n":
    vid = "option2NO.MOV"
    video()
    option2No = input("\nYou chose not to type your problem into Chat GPT and continue to work on your program by yourself. Do you ask for help from someone else? 'y' or 'n'\n")
    if option2No == "y":
        vid = "option2NOYES.MOV"
        video()
        print("\nYou ask for help from someone in your office, and the code is wildly successful! You get a pay raise and a new position as a problem solver.\n")
    if option2No == "n":
        vid = "option2NONO.MOV"
        video()
        print("\nYou chose not to ask for help. You become stressed out because of the problems in your code and as a result, you miss your deadline. Your boss fires you as this was a very important project.\n")