# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def Teleport():
    agent.teleport_to_player()

player.on_chat("come",Teleport)

def Forward(steps):
    agent.move(FORWARD, steps)

player.on_chat("fw", Forward)

def Back(steps):
    agent.move(BACK, steps)

player.on_chat("bk", Back)

def Left(steps):
    agent.move(LEFT, steps)

player.on_chat("left", Left)

def Right(steps):
    agent.move(RIGHT, steps)

player.on_chat("right", Right)

def TurnLeft():
    agent.turn(LEFT)

player.on_chat("tl", TurnLeft)

def TurnRight():
    agent.turn(LEFT)

player.on_chat("tr", TurnRight)

def Up(steps):
    agent.move(UP, steps)

player.on_chat("up", Up)

def Down(steps):
    agent.move(DOWN, steps)

player.on_chat("down", Down)


def ObstacleCourse():

    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 2)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)

player.on_chat("move", ObstacleCourse)

def Chat():
    for count in range(5):
        agent.move(FORWARD, 1)

player.on_chat("say", Chat)

def Chop(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()

player.on_chat("chop", Chop)

def Mine(length):
    for i in range(length):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("mine", Mine)

def Buildwall(height,width):
    for j in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(RIGHT, 1)
        agent.move(DOWN, height)

player.on_chat("wall", Buildwall)


def BuildRoof(height,width):
    for j in range(width):
        for i in range(height):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.move(RIGHT, 1)
        agent.move(BACK, height)

player.on_chat("roof", BuildRoof)

def Dig():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.collect_all()

player.on_chat("Dig", Dig)o