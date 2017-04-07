import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.ArrayList;

/**
 * 
 * @author seanwa
 *
 */
public class HelloJava {
	int solution (int N, String S, String T) {
		// bucket
		int [][] sCoord = new int[N][N];
		// soldier with seat
		int[][] tCoord = new int[N][N];
		// the max left seat
		int maxSeat = 0;
		//ArrayList maxCoord = new ArrayList(N*2);
		
		// check N whether meet the requirement
		if (N < 2 || N > 26 || (N % 2 != 0)) {
			System.out.println("0-Please check the input N!");
			return -1;
		}
		
		// check buckets
		if (S.trim().split(" ").length > N*N) {
			System.out.println("0-Please check the input S!");
			return -1;
		}
		
		// check soldier with seat
		if (T.trim().split(" ").length > N*N) {
			System.out.println("0-Please check the input T!");
			return -1;
		}
		
		// store the buckets and soldiers
		if (S.length() >= 2) {
			String[] tmpS = S.trim().split(" ");
			int numS = tmpS.length;
			for (int i = 0; i < numS; i++) {
				String rowS = tmpS[i].substring(0, 1);
				String colS = tmpS[i].substring(1, 2);
				if (tmpS[i].length() == 3) {
					rowS = tmpS[i].substring(0, 2);
					colS = tmpS[i].substring(2, 3);
				}
				int row = Integer.parseInt(rowS) - 1;
				int col = colS.toCharArray()[0] - 65;
				if (col >= N) {
					System.out.println("1-Please check the input S!");
					return -1;
				}
					
				sCoord[row][col] = -1;
				//System.out.println("sCoord["+row+"]["+col+"] is: "+sCoord[row][col]);
			}
		}
		if (T.length() >= 2) {
			String[] tmpT = T.trim().split(" ");
			int numT = tmpT.length;
			for (int i = 0; i < numT; i++) {
				String rowT = tmpT[i].substring(0, 1);
				String colT = tmpT[i].substring(1, 2);
				if (tmpT[i].length() == 3) {
					rowT = tmpT[i].substring(0, 2);
					colT = tmpT[i].substring(2, 3);
				}
				int row = Integer.parseInt(rowT) - 1;
				int col = colT.toCharArray()[0] - 65;
				if (col >= N) {
					System.out.println("1-Please check the input T!");
					return -1;
				}
				tCoord[row][col] = 1;
				//System.out.println("tCoord["+row+"]["+col+"] is: "+tCoord[row][col]);
			}
		}
		
		// prepare phase 1 ~ phase 4 needed info
		int[][] phaseInfo = new int[4][3];    // 0: phaseS number; 1: phaseT number; 2: left number
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 3; j++) {
				phaseInfo[i][j] = 0;
			}
		}
		// phase 1
		for (int i = 0; i < N/2; i++) {
			for (int j = 0; j < N/2; j++) {
				if (sCoord[i][j] == -1) {
					phaseInfo[0][0] += 1;
				}
				if (tCoord[i][j] == 1) {
					phaseInfo[0][1] += 1;
				}	
			}
		}
		phaseInfo[0][2] = N*N/4 - phaseInfo[0][0] -phaseInfo[0][1];
		// phase 2
		for (int i = 0; i < N/2; i++) {
			for (int j = N/2; j < N; j++) {
				if (sCoord[i][j] == -1) {
					phaseInfo[1][0] += 1;
				}
				if (tCoord[i][j] == 1) {
					phaseInfo[1][1] += 1;
				}	
			}
		}
		phaseInfo[1][2] = N*N/4 - phaseInfo[1][0] -phaseInfo[1][1];
		// phase 3
		for (int i = N/2; i < N; i++) {
			for (int j = 0; j < N/2; j++) {
				if (sCoord[i][j] == -1) {
					phaseInfo[2][0] += 1;
				}
				if (tCoord[i][j] == 1) {
					phaseInfo[2][1] += 1;
				}	
			}
		}
		phaseInfo[2][2] = N*N/4 - phaseInfo[2][0] -phaseInfo[2][1];
		// phase 4
		for (int i = N/2; i < N; i++) {
			for (int j = N/2; j < N; j++) {
				if (sCoord[i][j] == -1) {
					phaseInfo[3][0] += 1;
				}
				if (tCoord[i][j] == 1) {
					phaseInfo[3][1] += 1;
				}	
			}
		}
		phaseInfo[3][2] = N*N/4 - phaseInfo[3][0] -phaseInfo[3][1];
		 
		// start to calc the possible soldier number
		// phase 1
		for (int i = 0; i <= phaseInfo[0][2]; i++) {
			// phase 2
			for (int j = 0; j <= phaseInfo[1][2]; j++) {
				// phase 3
				for (int k = 0; k <= phaseInfo[2][2]; k++) {
					// phase 4
					for (int l = 0; l <= phaseInfo[3][2]; l++) {
						if (((phaseInfo[0][1] + i) + (phaseInfo[1][1] + j) == (phaseInfo[2][1] + k) + (phaseInfo[3][1] + l)) &&
							((phaseInfo[0][1] + i) + (phaseInfo[2][1] + k) == (phaseInfo[1][1] + j) + (phaseInfo[3][1] + l))) {
							// meet the condition
							maxSeat = i + j + k + l;
							//System.out.println("max soldiers are: "+maxSeat+" i: "+i+" j: "+j+" k: "+k+" l: "+ l);
						}
					}
				}
			}
		}
		
		//System.out.println("the max number of soldier's seat are: " + maxSeat);
		if ((maxSeat == 0)&&(phaseInfo[0][2]+phaseInfo[1][2]+phaseInfo[2][2]+phaseInfo[3][2] > 0)) {
			return -1;
		}
		else if (phaseInfo[0][2]+phaseInfo[1][2]+phaseInfo[2][2]+phaseInfo[3][2] == 0) {
			if ((phaseInfo[0][1] + phaseInfo[1][1] != phaseInfo[2][1] + phaseInfo[3][1]) ||
				(phaseInfo[0][1] + phaseInfo[2][1] != phaseInfo[1][1] + phaseInfo[3][1])) {
				return -1;
			}
		}
		return maxSeat;
	}
	
	public static void main (String [] args) {
		int ret = 0;
		int number = 0;
		String[] info = new String[3];
		
		HelloJava instance = new HelloJava();
		try {
			//number = System.in.read();
			BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
			info[0] = buf.readLine();
			info[1] = buf.readLine();
			info[2] = buf.readLine();
			number = Integer.parseInt(info[0]);
			buf.close();
			ret = instance.solution(number, info[1], info[2]);
			//instance.solution(13, "1B 1C 1D 4B 2A", "3B 2D");
			//instance.solution(4, "1B 1C 1D 1A 2A", "3B 3C");
			//instance.solution(4, "3B 3A 4A 4B", "");
			//instance.solution(4, "", "3B 3A 4A 4B");
			//instance.solution(2, "1A 1B 2A 2B", "");
			//instance.solution(2, "", "1A 1B 2A 2B");
			//instance.solution(2, "1A 2B 1B", "");
			//instance.solution(4, "1A 3A 1C 4D", "1B 2D 4A 3D");
			//instance.solution(2, "1A 1B", "2A 2B");
			System.out.println(ret);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
