import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class RandomizedSet {
    Map<Integer, Integer> map;
    List<Integer> list;
    Random random;

    public static void main(String[] args) {
        RandomizedSet r = new RandomizedSet();
        r.insert(1);
        r.remove(2);
        r.insert(2);
        r.insert(5);
        System.out.println(r.getRandom());
        r.insert(8);
        r.remove(1);
        r.remove(2);
        System.out.println(r.getRandom());
    }

    public RandomizedSet() {
        map = new HashMap<>();
        list = new ArrayList<>();
        random = new Random();
    }

    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }
        list.add(val);
        map.put(val, list.size() - 1);
        return true;
    }

    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }
        int index = map.get(val);
        int last = list.get(list.size() - 1);
        list.set(index, last);
        list.remove(list.size() - 1);
        map.put(last, index);
        map.remove(val);
        return true;
    }

    public int getRandom() {
        int r = random.nextInt(list.size());
        return list.get(r);
    }
}
