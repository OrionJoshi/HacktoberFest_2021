#include <stdio.h>
#include <stdlib.h>
struct node{
    struct node* prev;
    int data;
    struct node* next;
};
struct node* head=NULL;

void insbeg(int ele){
    struct node* temp = head;
    struct node* newnode = malloc(sizeof(struct node));
    if(newnode!=NULL){
        newnode->data=ele;
        newnode->prev=NULL;
        newnode->next=NULL;
        if(head!=NULL){
            temp=head->prev;
            // while(temp->next!=head){
            // temp=temp->next;
            // }
            temp->next=newnode;
            head->prev=newnode;
            newnode->prev=temp;
            newnode->next=head;
            head=newnode;
        }
        else{
            head=newnode;
        }
    }
    else{
        printf("Memory not allocated");
    }
}

void insend(int ele){
    struct node* temp=head;
    struct node* newnode = malloc(sizeof(struct node));
    if(newnode!=NULL){
        newnode->data=ele;
        newnode->prev=NULL;
        newnode->next=NULL;
        if(head!=NULL){
            if(head->next==NULL && head->prev==NULL){
                newnode->next=head;
                newnode->prev=temp;
                head->prev=newnode;
                temp->next=newnode;
            }
            else{
                temp=head->prev;
                // while(temp->next!=head){
                // temp=temp->next;
                // }
                newnode->next=head;
                newnode->prev=temp;
                head->prev=newnode;
                temp->next=newnode;
            }
        }
        else{
            head=newnode;
        }
    }
    else{
        printf("Memory not allocated");
    }
}

void display(){
    struct node* temp=head;
    printf("%d",temp->data);
    if(head==NULL){
        printf("List is Empty");
    }
    else{
        printf("Elements in the circular LL is ");
        while(temp->next!=head){
            printf("%d ",temp->data);
            temp=temp->next;
        }
        printf("%d ",temp->data);
    }
}

void insertpos(int posn,int ele){
    struct node* temp = head;
    struct node* newnode = malloc(sizeof(struct node));
    newnode->data=ele;
    newnode->prev=NULL;
    newnode->next=NULL;
    if(posn==1){
        temp=head->prev;
        temp->next=newnode;
        head->prev=newnode;
        newnode->prev=temp;
        newnode->next=head;
        head=newnode;
        printf("%d",head->data);
        // newnode->next=head;
        // newnode->prev=head->prev;
        // head->prev->next=newnode;
        // head->prev=newnode;
        // head=newnode;
    }
    else{
        int i=1;
        while(i<posn-1){
            temp=temp->next;
            i++;
        }
        newnode->next=temp->next;
        newnode->prev=temp;
        // newnode->next->prev=newnode;
        temp->next->prev=newnode;
        temp->next=newnode; 
    }
}



void del(int posn){
    struct node* temp=head;
    struct node* last=head->prev;
    struct node* deleted=malloc(sizeof(struct node));
    if(posn==1){
        deleted=head;
        head=head->next;
        head->prev=last;
        last->next=head;
        free(deleted);
    }
    else{
        int i=1;
        while(i<posn-2){
            temp=temp->next;
            i++;
        }
        deleted=temp->next;
        temp->next=deleted->next;
        deleted->next->prev=temp;
        free(deleted);
    }
    
}

int main(){
    int n,ele,posn;
    char input;
    scanf("%d",&n);
    scanf("%d",&ele);
    insbeg(ele);
    for(int i=0;i<n-1;i++){
        scanf("%d",&ele);
        insend(ele);
    }
    while(1){
        scanf("\n");
        scanf("%c",&input);
        switch((int)input){
        case 97:
        display();
        break;
        case 98:
        scanf("%d",&posn);
        scanf("%d",&ele);
        insertpos(posn,ele);
        break;
        case 99:
        scanf("%d",&posn);
        del(posn);
        break;
        }
        if(input='a'){
            break;
        }
    }
    return 0;
}