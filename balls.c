#include<stdio.h>

void main(){
    char password[30];

    printf("==== BALLS ====\n");
    printf(" balls ? ");
    scanf("%s", &password);

    if( strcmp(password, "balls") == 0 ){
        printf("BALLLS\n");
    } else {
        printf("Only balls allowed\n");
    }

    printf("==== B A L L S ==== ");
}
