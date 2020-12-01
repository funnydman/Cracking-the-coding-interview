TARGET = app

SRCS  = $(shell find . -type f -name '*.c')
HEADS = $(shell find ./include -type f -name '*.h')
OBJS = $(SRCS:.c=.o)

INCLUDES = -I./include
CCFLAGS = -O2 -Wall $(INCLUDES)
LDFLAGS =

all: $(TARGET)

$(TARGET): $(OBJS) $(HEADS)
	$(CX) $(LDFLAGS) -o $@ $(OBJS)

run: all
	@./$(TARGET)

.PHONY:  clean
clean:
	$(RM) $(OBJS) $(TARGET)

