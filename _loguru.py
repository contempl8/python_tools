# https://github.com/Delgan/loguru
from loguru import logger

logger.debug("Here it is")

def divide(x,y):
    return x/y

@logger.catch()
def main():
    divide(1,0)

if __name__ == "__main__":
    main()