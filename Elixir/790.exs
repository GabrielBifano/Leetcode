# Domino and Tromino Tiling
# Medium

defmodule Solution do
  @spec num_tilings(n :: integer) :: integer
  def num_tilings(n) when n == 2, do: 2
  def num_tilings(n) when n < 2, do: 1
  def num_tilings(n) do
    count(n, 2, 1, 1)
  end

  defp count(c, a3, _, _ ) when c < 3, do: a3
  defp count(c, a3, a2, a1) do
    count(c - 1, rem(a3 * 2 + a1, 1_000_000_007), a3, a2)
  end
end
