export default interface TaskInterface {
  id?: number;
  created_at?: Date;
  state?: string;
  title?: string;
  isChecked?: boolean;
}
