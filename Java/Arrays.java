
/**
 * Write a description of class Arrays here.
 *
 * @author (Joan Kehakae)
 * @version (Version 1 01/10/2021)
 */
import java.io.FileOutputStream;
import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.File;

public class Arrays
{

    static int [] array1=new int [1000];
    static int [] array2=new int [2000];
    static int [] array3=new int [3000];
    static  int [] array4=new int [4000];
    static  int [] array5=new int [5000];
    static int [] array6=new int [6000];
    static int [] array7=new int [7000];
    static int [] array8=new int [8000];
    static  int [] array9=new int [9000];
    static   int [] array10=new int [10000];

    /* Generating random numbers */

    private static int getRandomNumberInRange(int min, int max) {
        if (min >= max) {
            throw new IllegalArgumentException("max must be greater than min");
        }

        Random r = new Random();
        return r.nextInt((max - min) + 1) + min;
    }

    /*Writing To A Text File*/
    public static void Write(){
        try(FileWriter fw = new FileWriter("numbers.txt")) {
            for( int i=1; i<=10000; ++i) {
                fw.write(getRandomNumberInRange(1000,10000)+"\n");
            }
        }
        catch (IOException ioEx) {
            ioEx.printStackTrace();
        }
    }

    /* Read From File And Store Into An Array*/
    public static void Read(int [] array){
        try{
            Scanner scanner = new Scanner(new File("numbers.txt"));
            int [] arr = new int [array.length];
            int i = 0;
            while(scanner.hasNextInt())
            {
                arr[i++] = scanner.nextInt();
                System.out.println(arr[i++]);
            }
        }
        catch (Exception e) {

        }
    }

    /*Method For Printing*/
    public static void print(int [] array)
    {

        for(int i=0;i<array.length;i++)
        {
            System.out.println(array[i] );
        }
    }

    /*Bubblesort Algorith */
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

    /*Selection Sort Algorithm */
    public static void selectionSort(int[] arr){
        for (int i = 0; i < arr.length - 1; i++)
        {
            int index = i;
            for (int j = i + 1; j < arr.length; j++){
                if (arr[j] < arr[index]) {
                    index = j;//searching for lowest index
                }
            }
            int smallerNumber = arr[index];
            arr[index] = arr[i];
            arr[i] = smallerNumber;
        }
    }

    /*Insertion sort algorithm */
    public static void insertionSort(int array[]) {
        int n = array.length;
        for (int j = 1; j < n; j++) {
            int key = array[j];
            int i = j-1;
            while ( (i > -1) && ( array [i] > key ) ) {
                array [i+1] = array [i];
                i--;
            }
            array[i+1] = key;
        }
    }

    /*Merge sort algorithm */
    static void merge(int arr[], int beg, int mid, int end)
    {
        int l = mid - beg + 1;
        int r = end - mid;
        int LeftArray[] = new int [l];
        int RightArray[] = new int [r];
        for (int i=0; i<l; ++i)
            LeftArray[i] = arr[beg + i];
        for (int j=0; j<r; ++j)
            RightArray[j] = arr[mid + 1+ j];
        int i = 0, j = 0;
        int k = beg;
        while (i<l&&j<r) {
            if (LeftArray[i] <= RightArray[j])
            {
                arr[k] = LeftArray[i];
                i++;
            }
            else {
                arr[k] = RightArray[j];
                j++;
            }
            k++;
        }
        while (i<l)
        {
            arr[k] = LeftArray[i];
            i++;
            k++;
        }
        while (j<r)
        {
            arr[k] = RightArray[j];
            j++;
            k++;
        }
    } 

    static void sort(int arr[], int beg, int end)
    {
        if (beg<end)
        {
            int mid = (beg+end)/2;
            sort(arr, beg, mid);
            sort(arr , mid+1, end);
            merge(arr, beg, mid, end);
        }
    }

    /* Main function for executing the tasks */
    public static void  main (String [] args){
        Write();
        Read(array1);
       /* print(array1);*/
    }
}
