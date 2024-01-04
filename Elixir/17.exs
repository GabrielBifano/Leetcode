# Letter Combination of a Phone Number
# Medium

defmodule Solution do

  @keyboard %{
    "2" => ["a", "b", "c"],"3" => ["d", "e", "f"],
    "4" => ["g", "h", "i"],"5" => ["j", "k", "l"],
    "6" => ["m", "n", "o"],"7" => ["p", "q", "r", "s"],
    "8" => ["t", "u", "v"],"9" => ["w", "x", "y", "z"],
  }

  def keyboard(key) do
    Map.get(@keyboard, key, [])
  end

  def cartesian_product(l1, l2) do
    for x <- l1, y <- l2, do: y <> x
  end

  @spec letter_combinations(digits :: String.t) :: [String.t]
  def letter_combinations(""), do: []
  def letter_combinations(digits) do
    digits
    |> String.split("", trim: true)
    |> Enum.map(&keyboard/1)
    |> Enum.reduce(&cartesian_product/2)
  end
end
