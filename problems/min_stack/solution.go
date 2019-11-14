type MinStack struct {
    minIndex []int
    arr []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{nil, nil}
}


func (this *MinStack) Push(x int)  {
    this.arr = append(this.arr, x)
    if len(this.minIndex) == 0 || x < this.arr[this.minIndex[len(this.minIndex)-1]] {
        this.minIndex = append(this.minIndex, len(this.arr)-1)
    }
}


func (this *MinStack) Pop() {
    if this.minIndex[len(this.minIndex)-1] == len(this.arr)-1 {
        this.minIndex = this.minIndex[:len(this.minIndex)-1]
    }
    this.arr = this.arr[:len(this.arr)-1]
}


func (this *MinStack) Top() int {
    return this.arr[len(this.arr)-1]
}


func (this *MinStack) GetMin() int {
    return this.arr[this.minIndex[len(this.minIndex)-1]]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */