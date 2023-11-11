import java.io.*;
import java.util.Scanner;
import java.io.FileInputStream;


class Solution
{
	public static void main(String args[]) throws Exception
	{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T= Integer.parseInt(br.readLine());
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            String s = br.readLine();
            int cnt = 0;
            int status = (int)'0';
            for (int i = 0; i < s.length(); i++) {
                //first 1 c+=1 -> first 0 c+=1
                if ((int)s.charAt(i) != status) {
                    status = (int)s.charAt(i);
                    cnt += 1;
                }
            }
            
            System.out.printf("#%d %d\n", test_case, cnt);

		}
	}
}
