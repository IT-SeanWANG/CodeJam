//package june;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class ZhangShoubin_q1 {

	public static String[][] input(){
		 Scanner sca = new Scanner(System.in);
		 String str[] = new String[9];
		 ArrayList<String> array=new ArrayList<String>();
		 int count = 1;
		 while(count<=9){
	    	   array.add(sca.nextLine());
	    	   count+=1;
	       }
		 sca.close();
		 String[][]orig = new String[9][9];
		 for (int i = 0;i<array.size();i++) {
			str[i] = array.get(i);
			orig[i] = str[i].split(",");
		}
		 return orig;
	 }
	 public static boolean judgerow(String [][]shu){
		 int sum = 0;
		 for (int i = 0; i < shu.length; i++) {			
			 HashSet<String> row = new HashSet<String>();
			 for (int j = 0; j < shu[0].length; j++) {
				 row.add(shu[i][j]);
			 }
			 if(row.size()==9){
				 sum+=1;
			 }
		}
		 if(sum==9){
			 return true;
		 }else{			 
			 return false;
		 }
	 }
	 public static boolean judgecol(String[][]shu){
		 int sum = 0;
		 for (int i = 0; i < shu[0].length; i++) {			
			 HashSet<String> row = new HashSet<String>();
			 for (int j = 0; j < shu.length; j++) {
				 row.add(shu[j][i]);
			 }
			 if(row.size()==9){
				 sum+=1;
			 }
		}
		 if(sum==9){
			 return true;
		 }else{			 
			 return false;
		 }
	 }
	 public static boolean judgegong(String[][]shu){
		 String[][][]se2 = new String[9][3][3];
		 int row = 0;
			int sum = 0;
			String [][][]se= new String[3][3][9];
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					for (int j2 = 0; j2 < 9; j2++) {
						se[i][j][j2]=shu[row+j][j2];
					}
				}
				row+=3;
			}
			
			int col = 0;
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					for (int k = 0; k < 3; k++) {
						se2[i][j][k]=se[0][j][col+k];
					}
				}
				col+=3;
			}
			int col2 = 0;
			for (int i = 3; i < 6; i++) {
				for (int j = 0; j < 3; j++) {
					for (int k = 0; k < 3; k++) {
						se2[i][j][k]=se[1][j][col2+k];
					}
				}
				col2+=3;
			}
			int col3 = 0;
			for (int i = 6; i < 9; i++) {
				for (int j = 0; j < 3; j++) {
					for (int k = 0; k < 3; k++) {
						se2[i][j][k]=se[2][j][col3+k];
					}
				}
				col3+=3;
			}
		 for (int i = 0; i < 9; i++) {
			HashSet<String>set = new HashSet<String>();
			for (int j = 0; j < 3; j++) {
				for (int j2 = 0; j2 < 3; j2++) {					
					set.add(se2[i][j][j2]);
				}
			}
			if(set.size()==9){
				sum++;
			}
		}
		 if(sum==9){			 
			 return true;
		 }else{
			 return false;
		 }
	 }
	public static void main(String[] args) {
		String shu[][];
		shu = input();
		if(judgerow(shu)&&judgecol(shu)&&judgegong(shu)){
			System.out.println(1);
		}else{
			System.out.println(-1);
		}		
	}

}
