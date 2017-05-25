import pygame
import time
#screen = pygame.display.set_mode((600,400))

CLOCK = pygame.time.Clock()
clock_speed = 20

positions = {0,0,0} # Declare an array size of 3 to hold the positions of the 3 motors

running = True
pygame.init()
base_move_right = False
base_move_left = False
arm_move_up = False
arm_move_down = False
claw_move_close = False
claw_move_open = False

while running:
    try:
        for event in pygame.event.get():
            print('loop')
            if event.type == pygame.KEYDOWN:

                # Movement of the Base right and left using the left and right arrow key
                if event.key == pygame.K_LEFT:
                    print("left")
                    base_move_left = True
                elif event.key == pygame.K_RIGHT:
                    print("right")
                    base_move_right = True
                else:
                    base_move_right = False
                    base_move_left = False

                # Movement of the arm up and down using the up and down arrow key
                if event.key == pygame.K_UP:
                    arm_move_up = True
                elif event.key == pygame.K_DOWN:
                    arm_move_down = True
                else:
                    arm_move_up = False
                    arm_move_down = False

                # Open and close the claw using the 1 and 2 keys
                if event.key == pygame.K_1:
                    claw_move_close = True
                elif event.key == pygame.K_2:
                    claw_move_open = True
                else:
                    claw_move_close = False
                    claw_move_open = False
            
                # Quit the program if the Q key is pressed
                if event.key == pygame.K_q:
                    running = False
            
            # Move the base left or right
            if base_move_left:
                positions[0] += 5  # Increase the positon of the base by 5 degrees
                #BP.set_motor_position(PORT_A,postions[0])
                print ("Base postion: ", positions[0])
            elif base_move_right:
                positions[0] -= 5  # Decrease the positon of the base by 5 degrees
                #BP.set_motor_position(PORT_A,postions[0])
                print ("Base postion: ", positions[0])

            # Move the arm up or down
            if arm_move_up:
                positions[1] += 5
                #BP.set_motor_position(PORT_B,postions[1])
                print ("Arm position: ", positions[1])
            elif arm_move_down:
                positions[1] -= 5
                #BP.set_motor_position(PORT_B,postions[1])
                print ("Arm position: ", positions[1])

            # Move the claw open or close
            if claw_move_close:
                positions[2] += 5
                #BP.set_motor_position(PORT_C,postions[2])
                print ("Claw position: ", positions[2])
            elif claw_move_open:
                positions[2] -= 5
                #BP.set_motor_position(PORT_C,postions[2])
                print ("Claw position: ", positions[2])

            #set clock speed to limit cpu usage
            CLOCK.tick(clock_speed)
    except KeyboardInterrupt:
        print('CTRL C')
        running = False
print("QUIT")
#BP.set_motor_position(PORT_A,0)
#BP.set_motor_position(PORT_B,0)
#BP.set_motor_position(PORT_C,0)