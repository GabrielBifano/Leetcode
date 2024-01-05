# Domino and Tromino Tiling
# Medium

defmodule Solution do
  @spec num_tilings(n :: integer) :: integer
  def num_tilings(n) when n == 2, do: 2
  def num_tilings(n) when n < 2, do: 1
  def num_tilings(n) do
    count(n, 2, 1, 1)
  end

  defp count(c, dp1, _, _ ) when c < 3, do: dp1
  defp count(c, dp1, dp2, dp3) do
    count(c - 1, rem(dp1 * 2 + dp3, 1_000_000_007), dp1, dp2)
  end
end
