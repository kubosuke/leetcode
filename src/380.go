type RandomizedSet struct {
	mp map[int]bool
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		mp: make(map[int]bool),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.mp[val]; !ok {
		this.mp[val] = true
		return true
	}
	return false
}

func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.mp[val]; ok {
		delete(this.mp, val)
		return true
	}
	return false
}

func (this *RandomizedSet) GetRandom() int {
	l := len(this.mp)
	randNumber := rand.Intn(l)
	counter := 0

	for k := range this.mp {
		if counter == randNumber {
			return k
		}
		counter++
	}
	return -1
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
