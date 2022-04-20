from camera import Camera
class UserInterFace:
    def __init__(self):
        self.permission=None
        self.camera=Camera()
    def welcoming_message(self):
       
        print("         .-uuu-.")
        print("        / .===. \\")
        print("        \/ 6 6 \/")
        print("        ( \___/ )")
        print("   _ooo__\_____/______")
        print(" /                     \\")
        print("|Welcome to Future Alpha|")
        print(" \ _______________ooo_ /")
        print("""         |  |  |
         |_ | _|
         |  |  |
         |__|__|""")
        print("""         /-'Y'-\\
        (__/ \__)
        """)
        User_Name=input("Please enter your Name > ")
        print(f"welcome {User_Name} to your learning journey")
        
    def start_learning(self):
        permission=self.permission
        permission=input("Please provide permission to access the camera")
        if permission != None or "n" or "N":
            # check Camera Class
            self.camera.open_camera()


        else:
            #check
            print(".....")




        
interface=UserInterFace()
interface.welcoming_message()
interface.start_learning()
        