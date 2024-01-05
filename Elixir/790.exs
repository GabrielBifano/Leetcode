# Domino and Tromino Tiling
# Medium

defmodule Solution do
  @spec num_tilings(n :: integer) :: integer
  def num_tilings(n) do
    case n do
      0 -> 0
      1 -> 1
      2 -> 2
      _ -> count(n, 2, 1, 1)
    end
  end

  defp count(c, a3, _, _ ) when c < 3, do: a3
  defp count(c, a3, a2, a1) do
    count(c - 1, rem(a3 * 2 + a1, 1_000_000_007), a3, a2)
  end
end
