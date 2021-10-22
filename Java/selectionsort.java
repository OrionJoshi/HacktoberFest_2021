
public class SelectionSort{

static void bubbleSort(int[] arr) {
int n = arr.length;
int temp = 0;
for(int i=0; i < n; i++) {
for(int j=1; j < (n-i); j++) {
if(arr[j-1] > arr[j]) {
temp = arr[j-1];
arr[j-1] = arr[j];
arr[j] = temp;
}
}
}
}
int [] numbers = new int [5];

numbers[0]=4;
numbers[1]=2;
numbers[2]=0;
numbers[3]=6;
numbers[4]=1;


public static void main (String [] args )
{

}
}