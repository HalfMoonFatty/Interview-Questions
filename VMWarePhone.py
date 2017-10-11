OOM:
producer - consumer
1. allocating memory faster than GC 
2. don't even give GC the chance to collect garbage (allocate object in main and never used it)


HashTable vs HashMap:
HashTable is thread safe while HashMap is not


JVM or engineer:
Too low level shouldn't be concern by application engineer
GC is well tested and widely used so it is unlikely application engineers can write a better GC.
In general, whenever java libary support certain feature, the application engineer should rearly reinvent the wheel unless there is very specific goal. In terms of GC, the goal of GC is very general purpose, so it shouldn't be implemented by application engineers. 




def inPlaceReverseArray(arr):
    s, e = 0, len(arr)-1
    while s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    return arr


test = [1,2]
print inPlaceReverseArray(test)


===
public class Main {
	public static void ReverseArray(int[] arr) {
		for(int i = 0; i < data.length / 2; i++) {
		    int temp = data[i];
		    data[i] = data[data.length - i - 1];
		    data[data.length - i - 1] = temp;
		}
	}

	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 5};
		ReverseArray(arr);
		for (int i = 0; i < arr.length; ++i) {
			System.out.println(arr[i]);
		}
	}
}

===



