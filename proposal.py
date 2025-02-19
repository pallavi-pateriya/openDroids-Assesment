print("script started running...")
class RoboticArm:
      def __init__(self):
            self.position = [0,0,0]
            #x,y,z coordinates
            def move(self,x,y,z):
                self.position =[x,y,z]
                print(f"Arm moved to position: {self.position}")

                def pick_object(self):
                    print("object picked up!")

                    def drop_object(self):
                        print("object dropped!")
                        # Example usage
                        if __name__ =="__main__":
                            arm = RoboticArm()
                            #move arm to different positions
                            arm.moves(5,10,3)
                            arm.pick__object()
                            arm.moves(2,6,1)
                            arm.drop_object()
                     print("script completed succesfully")       