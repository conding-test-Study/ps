// 숫자라했는데 그냥 자연수라 치고 풀면 되는 문제였다. input.txt를 확인해볼걸 그랬나..
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    public static int pow(int n, int m, int result) {
        if (m == 0 || n == 1) { return result; }
        if (m < 0) {
            return pow(n, m - 1, result / n);            
        }
        else if (m > 0) {
            return pow(n, m - 1, result * n);
        }        
        return 1;
    }
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int t = sc.nextInt();
            int N = sc.nextInt();
            int M = sc.nextInt();
            
            int answer = pow(N, M, 1);
            System.out.printf("#%d %d\n", t, answer);
		}
	}
}
