# Maximum Twin Sum of a Linked List
# Medium

defmodule ListNode do
  @type t :: %__MODULE__{
    val: integer,
    next: ListNode.t() | nil
  }
  defstruct val: 0, next: nil
end


defmodule Solution do
  @spec pair_sum(head :: ListNode.t | nil) :: integer
  def pair_sum(head) do
    halve_it(head, head, [])
    |> maxsum(0)
  end

  defp halve_it(midpoint, nil, stack), do: {midpoint, stack}
  defp halve_it(midpoint, endpoint, stack) do
    halve_it(midpoint.next, endpoint.next.next, [midpoint.val | stack])
  end

  defp maxsum({midpoint, [x | stack]}, csum) do
    maxsum({midpoint.next, stack}, max(csum, midpoint.val + x))
  end
  defp maxsum(_, csum), do: csum
end
