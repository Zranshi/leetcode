package main

type ParkingSystem struct {
	left [4]int
}

func (s *ParkingSystem) AddCar(carType int) bool {
	if s.left[carType] > 0 {
		s.left[carType]--
		return true
	}
	return false
}
