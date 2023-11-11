import java.io.*;
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
        boolean flag;
        int cnt;
		T= 10;
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int len = Integer.parseInt(br.readLine());
            //2d arr init
            char[][] arr = new char[8][8];
            for (int i = 0; i < 8; i ++) {
                String s = br.readLine(); // string to char Array? string array?x no sep
                for (int j = 0; j < 8; j++) {
                    arr[i][j] = s.charAt(j);
                }
            }
            
            // w
            cnt = 0;
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8 - (len - 1); j++) {
                    flag = true;
                    for (int l = 0; l <= len / 2; l++) {
                        if (arr[i][j + l] != arr[i][j + len - 1 - l]) {
                            flag = false;
                        }
                    }
                    if (flag) {
                        cnt += 1;
                    }
                }
            }
            
             // w
            for (int j = 0; j < 8; j++) {
                for (int i = 0; i < 8 - (len - 1); i++) {
                    flag = true;
                    for (int l = 0; l <= len / 2; l++) {
                        if (arr[i + l][j] != arr[i + len - 1 - l][j]) {
                            flag = false;
                        }
                    }
                    if (flag) {
                        cnt += 1;
                    }
                }
            }
            System.out.printf("#%d %d\n", test_case, cnt);
		}
	}
}
