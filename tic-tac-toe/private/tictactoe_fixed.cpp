#include <iostream>
#include <random>
#include <ctime>

using namespace std;

const int size = 16;
int field[size][size];
int game;
bool gameflag;
const int N=86;
const int flagY[86]={7, 7, 6, 7, 6, 7, 6, 5, 6, 3, 7, 3, 5, 3, 3, 6, 2, 3, 3, 6, 2, 3, 3, 3, 5, 7, 3, 7, 7, 5, 6, 7, 6, 6, 5, 6, 3, 7, 5, 6, 7, 3, 5, 6, 7, 5, 6, 3, 7, 3, 7, 6, 7, 3, 5, 6, 6, 6, 6, 5, 3, 5, 6, 7, 3, 7, 5, 7, 6, 6, 7, 6, 6, 5, 6, 3, 6, 5, 7, 6, 3, 6, 3, 7, 3, 7};
const int flagX[86]={9, 4, 3, 4, 6, 11, 9, 15, 12, 0, 6, 3, 15, 7, 1, 3, 13, 7, 4, 3, 13, 7, 0, 3, 15, 6, 3, 2, 9, 15, 13, 5, 3, 8, 15, 3, 0, 10, 15, 9, 4, 5, 15, 13, 9, 15, 6, 4, 6, 0, 2, 9, 4, 3, 15, 7, 1, 13, 5, 15, 1, 15, 5, 6, 3, 2, 15, 0, 12, 1, 9, 5, 4, 15, 12, 0, 12, 15, 4, 8, 3, 2, 3, 3, 7, 13};


void show(){
    cout.width(4);
    cout << "";
    for (int i=0; i<size; i++){cout.width(4); cout << i;}
    cout << "   X" << endl << endl;
    for (int i=0; i<size; i++){
        cout.width(4);
        cout << i;
        for (int j=0; j<size; j++){cout.width(4); cout << (field[i][j]==0 ? '.':(field[i][j]==1 ? 'X':'O'));}
        cout << endl << endl;
    }
    cout << "   Y" << endl << endl;
}

bool go(int x, int y, int player){
    if (field[x][y] != 0) return false;
    field[x][y] = player;
    return true;
}

void playermove(){
    bool success = false;
    while (success == false){
        int x, y;
        cout << "<< X Y" << endl << "<< ";
        cin >> y >> x;
        if (0<=min(x, y) && max(x, y)<size)
        success = go(x, y, 2);
    }
}

bool checkfield(int i, int j, int di, int dj, int l){
    return (max(di*l, di*(l+4))<size-i)&&(min(di*l, di*(l+4))>=-i)&&(max(dj*l, dj*(l+4))<size-j)&&(min(dj*l, dj*(l+4))>=-j);
}

void aimove(){
    const int di[4]={1, 1, 0, -1};
    const int dj[4]={0, 1, 1, 1};
    int maxcost = 0;
    int maxi=0;
    int maxj=0;
    for (int i=0; i<size; i++)
        for (int j=0; j<size; j++)
            if (field[i][j]==0){
                int cost=0;
                for (int k =0; k<4; k++)
                    for (int l=-4; l<=0; l++)
                        if (checkfield(i, j, di[k], dj[k], l)){
                            int count[3]={0, 0, 0};
                            for (int m=0; m<5; m++) count[field[i+di[k]*(l+m)][j+dj[k]*(l+m)]]++;
                            if (count[1] == 0) cost+=(1 << 3*count[2]);//hard mod
                            if (count[2] == 0) cost+=(2 << 3*count[1]);//hard mod

                            //if (count[1] == 0) cost+=(count[2]);//easy mod(test)
                            //if (count[2] == 0) cost+=(count[1]);//easy mod(test)
                        }

                if (cost>maxcost && rand() % (5*N) - game < (4*N)){maxcost = cost; maxi=i; maxj=j;}
            }
    go(maxi, maxj, 1);
}

int gameisgoing(){
    const int di[4]={1, 1, 0, -1};
    const int dj[4]={0, 1, 1, 1};
    int playercanwin = 1;//draw
    for (int i=0; i<size; i++)
        for (int j=0; j<size; j++)
            for (int k =0; k<4; k++)
                if (checkfield(i, j, di[k], dj[k], 0)){
                    int count[3]={0, 0, 0};
                    for (int m=0; m<5; m++) count[field[i+di[k]*(m)][j+dj[k]*(m)]]++;
                    if (count[1] == 5) return 0;//player lose
                    if (count[1] == 0) playercanwin = 2;//isn't draw
                    if (count[2] == 5) return 3;//player win
                }

    return playercanwin;
}

int main() {
    srand(time(0));
    game = 0;
    while (game<N){
        for (int i=0; i<size; i++)
            for (int j=0; j<size; j++) field[i][j] = 0;
        int curentgame = game;
        go(flagX[game], flagY[game], 1);
        show();

        while (gameisgoing() == 2) {
            playermove();
            if (gameisgoing() != 3) aimove() else game++;
            show();
        }
        if (game == curentgame) {
            cout << "Try again";
            return 0;//player lose
         }
    }
    cout << "Congrats, this is the end";
    return 0;
}
