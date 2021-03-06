#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
 
typedef struct treap {
    struct treap* left;
    struct treap* right;
    int    key;
    int    data;
    int    prior;
} treap_t;
 
static   treap_t* treap_rotate(treap_t* p, int left);
treap_t* treap_insert(treap_t* p, int key, int data, treap_t** o);
treap_t* treap_delete(treap_t* p, int key);
treap_t* treap_find(treap_t* p, int key);
int      treap_min(const treap_t* p);
int      treap_max(const treap_t* p);
void     treap_clear(treap_t* p);
void     treap_print(FILE* _out, const char* fmt, const treap_t* p);
 
 
int main(void){
    char*    i;
    treap_t* p, *tr = NULL;
 
    char s[] = "ABCDEFGHOPWQAEQWERTYUIOPASDFGHJKLZWMKXCVBNMIOAAQEEKKKFZ";
    
    for(i = &s[0]; *i; ++i){
        p  = NULL;
        tr = treap_insert(tr, *i, 1, &p);
        if(p != NULL)
            ++(p->data);
            
    }
    
    printf("min key: %c\n",   treap_min(tr));
    printf("max key: %c\n\n", treap_max(tr));
 
    
    treap_print(stdout, "%c(%d)\t", tr);
    putchar('\n');
 
    
    tr = treap_delete(tr, 'A');
    tr = treap_delete(tr, 'O');
    tr = treap_delete(tr, 'Z');
    tr = treap_delete(tr, 'W');
 
    if(treap_find(tr, 'A') == NULL)
        puts("\nYes delete key 'A'.");
 
    putchar('\n');
    treap_print(stdout, "%c(%d)\t", tr);
    treap_clear(tr);
    return 0;
}
 

treap_t* treap_insert(treap_t* p, int key, int data, treap_t** o){
    if(p == NULL){
        p = (treap_t*)malloc(sizeof(treap_t));
        if(p != NULL){
            p->left  = p->right = NULL;
            p->key   = key;
            p->data  = data;
            p->prior = rand() % 128;
        }
        return p;
    } else if(key == p->key){
        if(o != NULL)
            *o = p;
        return p;
    } else if(key < p->key){
        p->left = treap_insert(p->left, key, data, o);
        if(p->left->prior > p->prior)
            p = treap_rotate(p, 0);
    } else {
        p->right = treap_insert(p->right, key, data, o);
        if(p->right->prior > p->prior)
            p = treap_rotate(p, 1);
    }
    return p;
}
 

treap_t* treap_delete(treap_t* p, int key){
    treap_t* t;
    if(p == NULL)
        return p;
    else if(key < p->key)
        p->left  = treap_delete(p->left, key);
    else if(key > p->key)
        p->right = treap_delete(p->right, key);
    else if(p->left == NULL){
        t = p->right;
        free(p);
        p = t;
    } else if(p->right == NULL){
        t = p->left;
        free(p);
        p = t;
    } else if(p->left->prior < p->right->prior){
        p = treap_rotate(p, 1);
        p->left = treap_delete(p->left, key);
    } else {
        p = treap_rotate(p, 0);
        p->right = treap_delete(p->right, key);
    }
    return p;
}
 

treap_t* treap_find(treap_t* p, int key){
    while(p != NULL){
        if(key == p->key)
            break;
        else if(key < p->key) {
            p = p->left;
        }
        else {
            p = p->right;
        }
    }
    return p;
}
 

int treap_min(const treap_t* p){
    if(p != NULL){
        while(p->left != NULL) {
            p = p->left;
        }
        return p->key;
    }
    return 0;
}
 

int treap_max(const treap_t* p){
    if(p != NULL){
        while(p->right != NULL) {
            p = p->right;
        }
        return p->key;
    }
    return 0;
}
 

void treap_clear(treap_t* p){
    if(p != NULL){
        if(p->left != NULL)
            treap_clear(p->left);
        if(p->right != NULL)
            treap_clear(p->right);
        free(p);
    }
}
 

void treap_print(FILE* _out, const char* fmt, const treap_t* p){
    if(p != NULL){
        if(p->left != NULL) {
            treap_print(_out, fmt, p->left);
        }

        fprintf(_out, fmt, p->key, p->data);
 
        if(p->right != NULL) {
            treap_print(_out, fmt, p->right);
        }
    }
}
 

static treap_t* treap_rotate(treap_t* p, int left){
    treap_t* q, *t;
    if(left){
        q        = p->right;
        t        = q->left;
        q->left  = p;
        p->right = t;
    } else {
        q        = p->left;
        t        = q->right;
        q->right = p;
        p->left  = t;
    }
    return q;
}