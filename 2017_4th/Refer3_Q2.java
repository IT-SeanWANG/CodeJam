//package june;

import java.util.Scanner;

public class ZhangShoubin_q2 {

	public static void main(String[] args) {
     Scanner sca = new Scanner(System.in);
     int zong = sca.nextInt();
     String danjia1 = sca.next();
     sca.close();
     String []danjia2 =danjia1.split(",");
     int []danjia3 = new int[danjia2.length];
     for (int i = 0; i < danjia2.length; i++) {
		danjia3[i] = Integer.parseInt(danjia2[i]);
	 }
     int sum1 = sum1(danjia3,danjia3.length,zong);     
     System.out.println(sum1);
	}

	public static int sum1(int[]price,int num,int zong){
		int[][]table = new int[num+1][zong+1];
		table[0][0]=1;
		
		for (int i = 1; i <= num; i++) {
			for (int j = 0; j <= zong; j++) {
				if(j<price[i-1]){
					table[i][j]=table[i-1][j];
				}else{
					table[i][j]=table[i-1][j]+table[i][j-price[i-1]];
				}
			}
		}
		int SUM = table[num][zong];
		return SUM;
	}
}
