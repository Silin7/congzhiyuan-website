declare module 'sortablejs' {
  export interface SortableEvent {
    oldIndex?: number
    newIndex?: number
    item: HTMLElement
    from: HTMLElement
    to: HTMLElement
  }

  export interface SortableOptions {
    animation?: number
    draggable?: string
    filter?: string
    onStart?: () => void
    onEnd?: (evt: SortableEvent) => void
    [key: string]: unknown
  }

  export default class Sortable {
    static create(el: HTMLElement, options?: SortableOptions): Sortable
    destroy(): void
  }
}
