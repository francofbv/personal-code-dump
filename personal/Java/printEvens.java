import java.io.*;
import java.util.Arrays;
public class printEvens {
    public static void main(String args[]){
        //given an array nums, the evenNums methods prints a new array of all even ints in nums
        int[] nums = new int[]{3, 1, 2, 5, 6, 2, 66, };
        evenNums(nums);
    }

        public static void evenNums(int[] nums){


            int count = 0;
            for (int i = 0; i < nums.length; i++){
                if (nums[i] % 2 == 0){
                    count++;
                }
            }
                int[] evens = new int[count];
                int evensIndex = 0;
                for (int i = 0; i < nums.length; i++){
                    if (nums[i] % 2 == 0){
                        evens[evensIndex] = nums[i];
                        evensIndex++;
                    }
                }
                System.out.println(Arrays.toString(evens));
        }
    }