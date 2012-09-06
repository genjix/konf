import sys, pygame
from datetime import datetime

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)
    currtime = datetime.today()
    end_hour, end_mins = [int(u) for u in sys.argv[1].split(":")]
    end_time = datetime(currtime.year, currtime.month, currtime.day,
                        end_hour, end_mins, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((1250, 600))
    font = pygame.font.SysFont("Comic Sans MS", 700)
    while currtime < end_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        currtime = datetime.today()
        remain_time = end_time - currtime
        # convert timedelta to mins and secs
        total_secs = remain_time.total_seconds()
        total_mins, total_secs = divmod(total_secs, 60)
        total_mins, total_secs = int(total_mins), int(total_secs)
        text = "%s:%s" % (total_mins, total_secs)
        label = font.render(text, 1, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(label, (0, 0))
        pygame.display.flip()
        pygame.time.wait(100)

