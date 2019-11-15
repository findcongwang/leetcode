import "fmt"

type Coord struct {
    r int
    c int
}

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
    visited := map[Coord]bool{}     // key = Coord{r, c}
    if len(image) == 0 {            // return empty image if it is empty
        return image
    }
    fillHelper(&image, sr, sc, image[sr][sc], newColor, &visited)
    return image
}

func fillHelper(image *[][]int, r int, c int, oldColor int, newColor int, visited *map[Coord]bool) {
    h := len(*image)
    w := len((*image)[0])
    
    fmt.Printf("filling from [%d, %d], which is currently %d\n", r, c, (*image)[r][c])
    
    for _, dr := range([]int{-1, 0 ,1}) {
        if dr+r > h-1 || dr+r < 0 {
            continue    // skip if out of bounds
        }
        if !(*visited)[Coord{dr+r, c}] && (*image)[dr+r][c] == oldColor {
            (*image)[dr+r][c] = newColor
            (*visited)[Coord{dr+r, c}] = true
            fillHelper(image, dr+r, c, oldColor, newColor, visited)
        }
    }
    for _, dc := range([]int{-1, 0 ,1}) {
        if dc+c > w-1 || dc+c < 0 {
            continue    // skip if out of bounds
        }
        if !(*visited)[Coord{r, dc+c}] && (*image)[r][dc+c] == oldColor {
            (*image)[r][dc+c] = newColor
            (*visited)[Coord{r, dc+c}] = true
            fillHelper(image, r, dc+c, oldColor, newColor, visited)
        }
    }
    return
}