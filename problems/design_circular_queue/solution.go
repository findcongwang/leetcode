type MyCircularQueue struct {
    Size int
    HeadIndex int
    TailIndex int
    Items []int
}


/** Initialize your data structure here. Set the size of the queue to be k. */
func Constructor(k int) MyCircularQueue {
    return MyCircularQueue{Size: k, Items: make([]int, k), HeadIndex: -1, TailIndex: -1}
}


/** Insert an element into the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) EnQueue(value int) bool {
    if this.IsEmpty() {
        this.Items[0] = value
        this.HeadIndex = 0
        this.TailIndex = 0
        fmt.Println(this)
        return true
    } else if !this.IsFull() {
        this.TailIndex = (this.TailIndex + 1) % this.Size
        this.Items[this.TailIndex] = value
        fmt.Println(this)
        return true
    } else {
        fmt.Println(this)
        return false
    }
}


/** Delete an element from the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) DeQueue() bool {
    if !this.IsEmpty() {
        this.Items[this.HeadIndex] = 0
        if this.HeadIndex == this.TailIndex {
            this.HeadIndex = -1
            this.TailIndex = -1
        } else {
            this.HeadIndex = (this.HeadIndex + 1) % this.Size    
        }
        fmt.Println(this)
        return true
    } else {
        fmt.Println(this)
        return false
    }
}


/** Get the front item from the queue. */
func (this *MyCircularQueue) Front() int {
    if this.IsEmpty() {
        return -1
    }
    return this.Items[this.HeadIndex]
}


/** Get the last item from the queue. */
func (this *MyCircularQueue) Rear() int {
    if this.IsEmpty() {
        return -1
    }
    return this.Items[this.TailIndex]
}


/** Checks whether the circular queue is empty or not. */
func (this *MyCircularQueue) IsEmpty() bool {
    return this.HeadIndex == -1
}


/** Checks whether the circular queue is full or not. */
func (this *MyCircularQueue) IsFull() bool {
    return (this.TailIndex + 1) % this.Size == this.HeadIndex
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */