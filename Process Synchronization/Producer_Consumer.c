#include<stdio.h>
#include<stdlib.h>

int mutex=1, full=0, empty=5, size=5;

int wait(int s) {
    return --s;
}

int signal(int s) {
    return ++s;
}

void producer() {
    mutex = wait(mutex);
    full = signal(full);
    empty = wait(empty);
    printf("\n\nProducer has produced the item...\n");
    mutex = signal(mutex);
}

void consumer() {
    mutex = wait(mutex);
    full = wait(full);
    empty = signal(empty);
    printf("\n\nConsumer has consumed the item...\n");
    mutex = signal(mutex);
}

int main() {
    printf("--- PRODUCER CONSUMER ---");
    printf("\nBuffer Size = %d", size);
    int ch;
    do {
        printf("\nCHOICES : ");
        printf("\n1 -> Producer");
        printf("\n2 -> Consumer");
        printf("\n3 -> Exit");
        printf("\nEnter your choice : ");
        scanf("%d", &ch);
        switch(ch) {
            case 1:
                if(mutex==1 && full<size)
                    producer();
                else
                    printf("\nBuffer is full...");
                break;
            case 2:
                if(mutex==1 && empty<size)
                    consumer();
                else
                    printf("\nBuffer is empty...");
                break;
            case 3:
                printf("\nExiting...");
                break;
            default:
                printf("\nEnter a valid choice....");
        }
    } while(ch != 3);
}