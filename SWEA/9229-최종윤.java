#scanner앞에서 잘 지우기  BufferReader를 하고 new Scanner가 안 지워져있으면  입력 이상함
#sc.nextInt,  int할떄 개행문자가 입력버퍼에 남아있어서 다음 sc.nextLine()하면 아무것도 입력 안 하고 넘어감

import java.util.Scanner;
import java.util.*;
import java.io.*;

public class Solution
{
	public static void main(String args[]) throws Exception
	{
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T = Integer.parseInt(br.readLine());
		

		for(int test_case = 1; test_case <= T; test_case++)
		{
		    
            StringTokenizer st = new StringTokenizer(br.readLine());
           
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int[] w = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                w[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(w);
            int s = 0;
            int e = n - 1;
            int maxSum = -1;
            while (s < e) {
                if (w[s] + w[e] < m) {
                    maxSum = Math.max(w[s] + w[e], maxSum);
                    s += 1;
                }
                else if (w[s] + w[e] == m) {
                    maxSum = m;
                    break;
                }
                else {
                    e -= 1;
                }
            }
		    System.out.printf("#%d %d", test_case, maxSum);
		    System.out.println();
			/////////////////////////////////////////////////////////////////////////////////////////////
			/*
				 이 부분에 여러분의 알고리즘 구현이 들어갑니다.
			 */
			/////////////////////////////////////////////////////////////////////////////////////////////

		}
	}
}
