"""
排序集锦
"""

"""
稳定排序：当已经确定的位置，顺序不会发生改变，不稳定排序相反

稳定排序：
冒泡，插入排序 O(n^2)
归并排序 O(nlogn)
计数排序 O(n+k)
桶排序 O(n+k)
基数排序 O(n+k)

不稳定排序
选择排序 O(n^2)
快速排序 O(nlogn)
堆排序 O(nlogn)



# 1.算法

算法就是解决问题的步骤。
给定数据，通过算法输出望的结果。
核心是：注重效率和空间成本。

## 1.1.排序算法
### 快速排序

平均复杂度O（log2N），最坏0（n2）

```java
package com.ygl.algorithm.sort;

import lombok.extern.slf4j.Slf4j;
import java.util.Arrays;

@Slf4j
public class QuickSort {
	private static int count = 0;

	public static void main(String[] args) {

		int[] arr = {3, 7, 6, 5, 4, 2, 1,};
		QKSort(arr, 0, arr.length - 1);
	}

	/**
	 * 快速排序是（挖坑法）是挖坑填数 + 分治来实现。
	 * 先从数列中取出一个数作为基准数。
	 * 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
	 * 再对左右区间重复第二步，直到各区间只有一个数。
	 *
	 * @param arr
	 * @param start
	 * @param end
	 */
	private static void QKSort(int[] arr, int start, int end) {
		/*条件判断*/
		if (start >= end) {
			return;
		}
		int left = start, right = end;

		//最左端元素为基元
		int temp = arr[left];

		//基元比较，在循环结束后基元插入数据，作为二分的基准点。
		while (left < right) {
			//最右端查找，比基元大的元素，不动，坐标左移，继续寻找比基元小的元素
			while (left < right && arr[right] >= temp) {
				right--;
			}

			//1、找到比基元小的，该元素赋值给基元位置，也就是最左端
			//2、未发现比基元小的元素，最右端元素放到基元位置，也就是最左端
			arr[left] = arr[right];

			//最左端查找，比基元小的元素，不动，坐标右移，寻找比基元大的元素
			while (left < right && arr[left] <= temp) {
				left++;
			}

			//1、找到比基元小的，左移互换，继续循环。直到左边都比基元小
			//2、未发现比基元小的元素，基元移动到最右端，也就是left==right 结束循环，此时是最坏的情况，那就是最大数在最左端
			arr[right] = arr[left];

		}
		//循环后right = left
		//循环后的left的值正是temp的位置，为arr[left]的值是temp的下一个元素 必然是重复的
		//此时的数据中并没有temp的位置 temp赋值给left做基元, 基元作为边界将数组分为两边。


		//基元赋值给left 重回数组
		arr[left] = temp;
		QKSort(arr, start, left - 1);
		QKSort(arr, left + 1, end);
		//输出
		log.info(++count + "");
		log.info(Arrays.toString(arr));
	}
}
```
### 堆(树)排序

大根堆是正序排序。小根堆倒序排序。

平均复杂度O（log2N），数值不能重复。否则无法构成二叉树

```java
package com.ygl.algorithm.sort;

import java.util.Arrays;

/**
 * @USER: rookie_ygl
 * @DATE: 2020/6/1
 * @TIME: 23:00
 * @DESC: open stack
 *
 * 堆排序的数据结构是根堆
 *
 * 从小到大排 就是大根堆。从大到小，就是小根堆
 *
 * 大根堆存在 arr[i]>=arr[2i+1] && arr[2i+2]
 *
 * 左右节点占一个元素，为空也占位
 **/
public class StackTreeSort {
    public static void main(String[] args) {
        int[] arr = new int[]{7, 2, 10, 4, 5, 6, 1};
        heapSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    /**
     * 堆排序 升序
     *
     * @param array 待调整堆
     */
    public static void heapSort(int[] array) {
        //把无序数组构建最大堆
        //寻找非叶子节点，只有非叶子节点需要调整
        //根据二叉树的特性，非叶子节点个数是n/2
        for (int i = (array.length) / 2 - 1; i >= 0; i--) {
            downAdjust(array, i, array.length);
        }

        //输出最大堆
        System.out.println(Arrays.toString(array));

        //倒叙遍历数组，循环删除堆顶元素，与数组尾部元素交换，
        //调整结束就是排序好的数组
        for (int i = array.length - 1; i > 0; i--) {
            //尾部元素和头部元素交换
            int temp = array[i];
            array[i] = array[0];
            array[0] = temp;

            //下沉调整最大堆
            downAdjust(array, 0, i);
        }
    }

    /**
     * 堆 下沉
     *
     * @param array       待调整的堆
     * @param parentIndex 需要下沉的父节点
     * @param length      堆的有效大小
     */
    public static void downAdjust(int[] array, int parentIndex, int length) {
        //temp 保存父节点的值 用于最后赋值
        int temp = array[parentIndex];
        int childIndex = 2 * parentIndex + 1;

        //防止角标越界
        while (childIndex < length) {
            //如果有右孩子，且左孩子大于右孩子的值，则定位到右孩子
            if (childIndex + 1 < length && array[childIndex + 1] > array[childIndex]) {
                childIndex++;
            }

            //如果父节点大与任何一个孩子的值，则直接跳出
            if (temp >= array[childIndex]) {
                break;
            }

            //如果父节点不是最大，就和当前子节点交换位置
            //一次能确定一个父节点和两个子节点
            array[parentIndex] = array[childIndex];
            parentIndex = childIndex;
            childIndex = 2 * childIndex + 1;
        }
        array[parentIndex] = temp;
    }
}
```



### 冒泡排序

```java
package com.algorithm.sort;

public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {1, 6, 8, 7, 3, 5, 16, 4, 8, 36, 13, 44};
        bubbleSort(arr);
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }

    /**
     * 冒泡排序
     * 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
     * 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
     * 针对所有的元素重复以上的步骤，除了最后一个。
     * 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
     *
     * @param arr
     */
    public static void bubbleSort(int[] arr) {
        int temp = 0;
        int size = arr.length;
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - 1 - i; j++) {
                if (arr[j] > arr[j + 1])
                //交换两数位置
                {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
```
### 选择排序算法
```java
package com.algorithm.sort;

/**
 * @Author: open stack
 * @Author: ygl
 * @Date: 2020/5/7 22:44
 * @Desc:
 */
public class SelectSort {
	public static void main(String[] args) {
		int[] arr = {1, 6, 8, 7, 3, 5, 16, 4, 8, 36, 13, 44};
		selectSort(arr);
		for (int i : arr) {
			System.out.print(i + " ");
		}
	}

	/**
	 * 选择排序算法
	 * 在未排序序列中找到最小元素，存放到排序序列的起始位置
	 * 再从剩余未排序元素中继续寻找最小元素，然后放到排序序列末尾。
	 * 以此类推，直到所有元素均排序完毕。
	 * <p>
	 * 一边正向遍历存值，一遍逆向取值
	 */
	public static void selectSort(int[] numbers) {
		int size = numbers.length; //数组长度
		int temp = 0; //中间变量
		for (int i = 0; i < size; i++) {
			int k = i;   //待确定的位置 也就是 numbers[j] < numbers[i] 就调换位置
			//选择出应该在第i个位置的数
			for (int j = size - 1; j > i; j--) {
				if (numbers[j] < numbers[k]) {
					k = j;
				}
			}
			//交换两个数
			temp = numbers[i];
			numbers[i] = numbers[k];
			numbers[k] = temp;
		}
	}
}
```
### 插入排序
```java
package com.algorithm.sort;

/**
 * @Author: open stack
 * @Author: ygl
 * @Date: 2020/5/7 22:47
 * @Desc:
 */
public class InsertSort {
	public static void main(String[] args) {
		int[] arr = {1, 6, 8, 7, 3, 5, 16, 4, 8, 36, 13, 44};
		insertSort(arr);
		for (int i : arr) {
			System.out.print(i + " ");
		}
	}

	/**
	 * 插入排序
	 * 是在一个已经有序的小序列的基础上，一次插入一个元素。
	 * 当然，刚开始这个有序的小序列只有1个元素，就是第一个元素。比较是从有序序列的末尾开始，
	 * 也就是想要插入的元素和已经有序的最大者开始比起，如果比它大则直接插入在其后面，
	 * 否则一直往前找直到找到它该插入的位置。如果碰见一个和插入元素相等的，
	 * 那么插入元素把想插入的元素放在相等元素的后面。所以，相等元素的前后顺序没有改变，
	 * 从原无序序列出去的顺序就是排好序后的顺序，所以插入排序是稳定的。
	 */
	public static void insertSort(int[] numbers) {
		int size = numbers.length;
		int temp = 0;
		int j = 0;
		for (int i = 0; i < size; i++) {
			temp = numbers[i];
			//假如temp比前面的值小，则将前面的值后移
			for (j = i; j > 0 && temp < numbers[j - 1]; j--) {
				numbers[j] = numbers[j - 1];
			}
			numbers[j] = temp;
		}
	}
}
```
## 1.2.动态规划

### 爬楼梯问题

### 两点路径问题

### 找零问题

### 找零最优解问题

### 01背包问题

### 斐波那契

```java
public static void main(String[] args) {
    //输出第n项的值
    Scanner scan = new Scanner(System.in);
    System.out.println("请输入你需要的项数N；回车:");
    int n = Integer.parseInt(scan.nextLine().trim());
    System.out.println("f("+n+")="+f(n));
    //输出前n项所有数据 每10个换一行
    for(int i=1;i<=n;i++){
        System.out.print(f(i)+"\t");
        if(i%10==0){
            System.out.println();
        }
    }
    
    /**
    * 传入参数n  返回值类型为long,若为int可能出现溢出
    */
    public static long flib(int n){
        if(n == 1 || n == 2){//参数1或者2时
            return 1;
        }else{
            return flib (n - 1) + flib (n - 2);
        }
    }

}
```



# 2.算法实战

## 2.1.控制形状

```java
package Sort;

public class ShapeDemo {
    public static void main(String[] args) {
        sanjiao(5);
        lingxing(7);
    }
    public static void sanjiao(int lay) {
        for (int i = 1; i <= lay; i++)//控制打印的行数
        {
            for (int a = 0; a < lay - i; a++) {
                System.out.print(" ");//打印空格
            }
            for (int b = 1; b <= i * 2 - 1; b++) {
			//判断是否是第一或最后一行
                if (i == 1 || i == lay)
                {
                    System.out.print("*");
                } else {
			//判断是否是本行第一个或最后一个字符

                 if (b == 1 || b == i * 2 - 1){
                        System.out.print("*");
                    } else {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println();//输出回车
        }
    }
    public static void lingxing(int lay) {
        for (int m = 1; m <= (lay + 1) / 2; m++)//正序输出上半部分
        {
            for (int b = 1; b <= (lay + 1) / 2 - m; b++)//输出空格
            {
                System.out.print(" ");
            }
            for (int c = 1; c <= m * 2 - 1; c++) {
                System.out.print("*");
            }
            System.out.println();//换行
        }
        for (int d = (lay + 1) / 2 - 1; d >= 1; d--)//倒序输出下半部分
        {
            for (int b = 1; b <= (lay + 1) / 2 - d; b++)//输出空格
            {
                System.out.print(" ");
            }
            for (int c = (lay + 1) / 2 - d; c <= (lay + 1) / 2 - 2 + d; c++)//(lay+1)/2-1即为下半个三角形
            {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}

```
## 2.2.找出1-6的所有数字组合

```

```


"""
