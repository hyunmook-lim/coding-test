import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<Integer, ArrayList<ArrayList<Character>>> wildCountMap = new HashMap<>();
        ArrayList<ArrayList<Character>> ans = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            ArrayList<Character> DNA = new ArrayList<>();
            int count = 0;

            String input = br.readLine();

            for (int j = 0; j < M; j++) {
                Character core = input.charAt(j);
                if (core.equals('.')) count += 1;
                DNA.add(core);
            }
            if (wildCountMap.get(count) == null) {
                ArrayList<ArrayList<Character>> list = new ArrayList<>();
                list.add(DNA);
                wildCountMap.put(count, list);
            } else {
                wildCountMap.get(count).add(DNA);
            }
        }

//        System.out.println("wildCountMap = " + wildCountMap);
//        System.out.println("======================================");

        for (int i = M; i >= 0; i--) {
            ArrayList<ArrayList<Character>> list = wildCountMap.get(i);
            if (list == null) continue;

            for (ArrayList<Character> newDna : list) {
//                System.out.println("newDna = " + newDna);
                boolean merged = false;

                for (int j = 0; j < ans.size(); j++) {
                    if (check(newDna, ans.get(j))) {

                        ans.add(merge(newDna, ans.get(j)));
                        ans.remove(j);
                        merged = true;
                        break;
                    }
                }

                if (!merged) ans.add(newDna);
            }
        }

        System.out.println(ans.size());
    }

    protected static boolean check(ArrayList<Character> first, ArrayList<Character> second) {
        boolean flag = true;

        for (int i = 0; i < first.size(); i++) {
            Character firstChar = first.get(i);
            Character secondChar = second.get(i);

            if (firstChar.equals('.') || secondChar.equals('.')) continue;

            if (!firstChar.equals(secondChar)) {
                flag = false;
                break;
            }
        }

        return flag;
    }

    protected static ArrayList<Character> merge(ArrayList<Character> first, ArrayList<Character> second) {
        ArrayList<Character> merged = new ArrayList<>();
        for (int i = 0; i < first.size(); i++) {
            Character firstChar = first.get(i);
            Character secondChar = second.get(i);

            if (firstChar.equals('.')) {
                merged.add(secondChar);
            } else {
                merged.add(firstChar);
            }
        }

        return merged;
    }
}