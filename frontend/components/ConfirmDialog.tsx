"use client";

interface Props {
  message: string;
  onConfirm: () => void;
}

export default function ConfirmDialog({
  message,
  onConfirm,
}: Props) {
  function handleDelete() {
    const ok = window.confirm(message);

    if (ok) {
      onConfirm();
    }
  }

  return (
    <button
      onClick={handleDelete}
      style={{
        background: "#dc2626",
        color: "white",
        border: "none",
        padding: "8px 15px",
        cursor: "pointer",
      }}
    >
      Delete
    </button>
  );
}