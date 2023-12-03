from os import system
QUBO_COMMAND = 'java -Dfile.encoding=UTF-8 --enable-preview -jar qubo.jar -range {} ports 26000-28000 -th 8000 -ti 700'

while True:
    system(QUBO_COMMAND.format(input('')))
