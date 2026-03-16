import { useRef, useCallback } from 'react'

export const useSSE = (onMessage: (data: string) => void) => {
  const eventSourceRef = useRef<EventSource | null>(null)

  const connect = useCallback((url: string) => {
    disconnect()
    
    const eventSource = new EventSource(url)
    eventSourceRef.current = eventSource

    eventSource.onmessage = (event) => {
      onMessage(event.data)
    }

    eventSource.onerror = () => {
      console.error('SSE 连接错误')
      disconnect()
    }
  }, [onMessage])

  const disconnect = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close()
      eventSourceRef.current = null
    }
  }, [])

  return { connect, disconnect }
}
