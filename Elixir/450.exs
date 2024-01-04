# Doesnt work. I will correct it futurely

defmodule TreeNode do
  @type t :: %__MODULE__{
    val: integer,
    left: TreeNode.t() | nil,
    right: TreeNode.t() | nil
  }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec delete_node(root :: TreeNode.t | nil, key :: integer) :: TreeNode.t | nil
  def delete_node(root, key) do
    get_node(root, key)
    |> del_node(key)
    root
  end

  defp get_node(node, key) do
    cond do
      nil == node -> nil
      key == node.val -> node
      key <  node.val -> get_node(node.left,  key)
      key >  node.val -> get_node(node.right, key)
    end
  end

  defp del_node(nil, _), do: nil
  defp del_node(node, key) do
    case {node.left, node.right} do
      {nil,   nil}  -> node = nil
      {left,  nil}  -> node = node.left
      {nil, right}  -> node = node.right
      {left, right} -> node = swap_for_successor(node)
    end
  end

  defp swap_for_successor(node) do
    succ = successor(node, node.right)
    node = %{node | right: succ.right}
  end

  defp successor(node, nil),  do: node
  defp successor(node, left), do: successor(node.left, left.left)
end
